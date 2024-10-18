from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField( max_length=200)
    item_desc=models.CharField(max_length=200)
    image_price=models.IntegerField(max_length=10,default=55)
    item_image=models.CharField(max_length=500,default='https://png.pngtree.com/png-vector/20190223/ourmid/pngtree-vector-picture-icon-png-image_695350.jpg')
    
    def __str__(self):
        return self.item_name
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"item_id": self.pk})
    
    
