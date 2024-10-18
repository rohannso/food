from django import forms
from .models import Item

class itemform(forms.ModelForm):
    
    class Meta:
        model=Item
        fields = ['item_name','image_price','item_desc','item_image']
        