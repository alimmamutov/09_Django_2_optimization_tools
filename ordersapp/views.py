# Create your views here.
from dataclasses import fields

from django.db import transaction
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from baskets.models import Basket
from mainapp.mixin import BaseClassContextMixin
from mainapp.models import Product
from ordersapp.forms import OrderItemsForm, OrderForm
from ordersapp.models import Order, OrderItem


class OrderListView(ListView, BaseClassContextMixin):
    model = Order
    title = 'Geekshop | Список заказов'
    # Здесь мы не указали  явно темплейт, т.к. он подставится автоматически при правильном названии темплейта
    # <название модели>_<тип вьюхи>.html

    def get_queryset(self):
        return Order.objects.filter(is_active=True, user=self.request.user)


class OrderCreateView(CreateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'Geekshop | Создание заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, OrderItemsForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            # basket_item = Basket.objects.filter(user=self.request.user)
            basket_item = Basket.objects.filter(user=self.request.user).select_related()
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem, OrderItemsForm, extra=basket_item.count())
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                # basket_item.delete() закомментил, чтобы новый заказ не очищал корзину TODO: remove comments
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()

        return super(OrderCreateView, self).form_valid(form)


class OrderDeleteView(DeleteView, BaseClassContextMixin):
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'Geekshop | Удаление заказа'


class OrderUpdateView(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'Geekshop | Редактирование заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderUpdateView, self).get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, OrderItemsForm, extra=0)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)  # instance указывает какой именно объект мы изменяем
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

            if self.object.get_total_cost() == 0:
                self.object.delete()

        return super(OrderUpdateView, self).form_valid(form)


class OrderDetailView(DetailView, BaseClassContextMixin):
    model = Order
    title = 'Geekshop | Просмотр заказа'


def order_status_change(request, pk, new_status):
    order = get_object_or_404(Order, pk=pk)  # здесь получается объект модели по первичному ключу
    order.change_status(new_status)
    return HttpResponseRedirect(reverse('orders:list'))


def order_next_status(request, pk):
    new_status = 0
    order = get_object_or_404(Order, pk=pk)
    for num, el in enumerate(Order.ORDER_STATUS_CHOICES):
        if el[0] == order.status:
            new_status = num + 1 if len(Order.ORDER_STATUS_CHOICES) > num + 1 else 0
            break
    order.change_status(new_status)
    return HttpResponseRedirect(reverse('orders:list'))


@receiver(pre_delete, sender=OrderItem)
@receiver(pre_delete, sender=Basket)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity  # Возвращаем товары на склад
    instance.save()


@receiver(pre_save, sender=OrderItem)
@receiver(pre_save, sender=Basket)
def product_quantity_update_save(sender, instance, **kwargs):
    if instance.pk:
        get_item = instance.get_item(int(instance.pk))
        instance.product.quantity -= instance.quantity - get_item
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


# контроллер получения цены продукта если есть pk, если нет то 0
def product_price(request,pk):
    if request.is_ajax():
        product_item = Product.objects.filter(pk=pk).first()
        if product_item:
            return JsonResponse({'price': product_item.price})
        return JsonResponse({'price': 0})
