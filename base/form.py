from .models import *
from django.forms.models import ModelForm



class ClientForm(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'
        exclude = ['tracking_id']


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['receiver']