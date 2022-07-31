from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    price = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ProPrice', default=1)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user} {self.product} {self.price} {self.quantity}'
    
