from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
 product_name = models.CharField(max_length=50) 
 product_price =  models.IntegerField() 
 product_img = models.ImageField(upload_to='images/') 

 def __str__(self):
  return self.product_name

class Cart(models.Model):
 cartuser=models.ForeignKey(User, on_delete=models.CASCADE, default=True)
 name = models.CharField(max_length=50) 
 price =  models.IntegerField() 
 
 img = models.ImageField(upload_to='images/') 

 def __str__(self):
  return self.name