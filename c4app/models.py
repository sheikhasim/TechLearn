from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse


# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


#class Orders(models.Model):
    #order_id=models.AutoField(primary_key=True)
    #items_json=models.CharField(max_length=5000)
    #amount=models.IntegerField(default=0)
    #name=models.CharField(max_length=90)
    #email=models.EmailField(max_length=111)
    #phone=models.CharField(max_length=111)
    #city=models.CharField(max_length=111)
    #state=models.CharField(max_length=111)-->
