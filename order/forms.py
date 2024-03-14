from django.forms import ModelForm
from order.models import Order, ShopCart

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']

 # def __init__(self, *args, **kwargs):
 #        super(OrderForm, self).__init__(*args, **kwargs)
 #        self.fields.update(UserForm2().fields)
 #        self.fields.update(UserProfileForm2().fields)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']