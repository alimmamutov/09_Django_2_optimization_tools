from django.urls import path

from ordersapp.views import OrderListView, OrderCreateView, OrderDeleteView, OrderUpdateView, OrderDetailView, \
    order_status_change, order_next_status

app_name = 'ordersapp'
urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('read/<int:pk>/', OrderDetailView.as_view(), name='read'),
    # path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('order_status_change/<int:pk>/<int:new_status>/', order_status_change, name='order_status_change'),
    path('next_status/<int:pk>/', order_next_status, name='next_status'),
]
