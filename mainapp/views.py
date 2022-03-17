from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

import json
import os

from django.views.decorators.cache import cache_page, never_cache
from django.views.generic import DetailView
from django.conf import settings
from django.core.cache import cache
from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.
def _get_link():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return ProductCategory.objects.all()


def _get_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')


def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


@cache_page(3600)
@never_cache
def products(request,id_category=None,page=1):

    context = {
        'title': 'Geekshop | Каталог',
    }

    if id_category:
        # products= Product.objects.filter(category_id=id_category)
        products= Product.objects.filter(category_id=id_category).select_related()  # Здесь мы передаем в контект все связанные поля, чтобы в дальнейшем не обращаться к ним через точку
    else:
        # products = Product.objects.all()
        products = Product.objects.all().select_related()
        # products = Product.objects.all().prefetch_related()  # при формировании связи многие ко многим - используем prefetch_related

    # products = _get_product()
    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    # context['categories'] = ProductCategory.objects.all()
    context['categories'] = _get_link()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'mainapp/detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductDetail, self).get_context_data(**kwargs)
    #     product = self.get_object()
    #     context['product'] = product
    #     return context

