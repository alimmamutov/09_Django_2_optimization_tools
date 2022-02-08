# Create your views here.
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, DetailView


class OrderListView(ListView):
    pass


class OrderCreateView(CreateView):
    pass


class OrderDeleteView(DeleteView):
    pass


class OrderUpdateView(UpdateView):
    pass


class OrderDetailView(DetailView):
    pass


def order_forming_complete(request, pk):
    pass
