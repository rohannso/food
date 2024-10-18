from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='profilepic.jpg',upload_to='profiles')
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
