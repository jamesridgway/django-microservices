from crispy_forms.helper import FormHelper
from django import forms

from orders.models import Order


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number',)

    def __init__(self, *args, **kwargs):
        super(NewOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-6'
