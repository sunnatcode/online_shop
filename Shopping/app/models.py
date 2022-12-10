from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

class Product(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price       = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/', null=True)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

class Order(models.Model):
    cart_id    =  models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity   =  models.FloatField()