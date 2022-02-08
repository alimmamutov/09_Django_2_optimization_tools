from django.forms import forms
from sqlalchemy.testing import exclude

from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('user', )

    def __init__(self,*args,**kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name , field in self.fields.items():
            if field_name != 'status':
                field.widget.attrs['class'] = 'form-control py-4'
            else:  # т. к. поле статус - поле выбора - нельзя исп-ть класс py-4
                field.widget.attrs['class'] = 'form-control'


class OrderItemsForm(forms.ModelForm):

    price = forms.CharField(label='цена', required=false)

    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(OrderItemsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
