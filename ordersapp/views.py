# Create your views here.
from dataclasses import fields

from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView

from baskets.models import Basket
from mainapp.mixin import BaseClassContextMixin
from ordersapp.models import Order, OrderItem


class OrderListView(ListView, BaseClassContextMixin):
    model = Order
    title = 'Geekshop | Список заказов'
    # Здесь мы не указали  явно темплейт, т.к. он подставится автоматически при правильном названии темплейта
    # <название модели>_<тип вьюхи>.html

    pass


class OrderCreateView(CreateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'Geekshop | Создание заказа'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, extra=3)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket = Basket.objects.filter(user=self.request.user)

    def form_valid(self, form):
        pass


class OrderDeleteView(DeleteView, BaseClassContextMixin):
    model = Order
    success_url = reverse_lazy('orders:list')
    title = 'Geekshop | Удаление заказа'


class OrderUpdateView(UpdateView):
    pass


class OrderDetailView(DetailView, BaseClassContextMixin):
    model = Order
    title = 'Geekshop | Просмотр заказа'


def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)  # здесь получается объект модели по первичному ключу
    order.status = Order.SEND_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))
