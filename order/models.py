from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    order_status = (
        ('pending','pending'),
        ('placed','placed'),
        ('dispatched','dispatched'),
        ('delivered','delvered'),
        ('cancelled','cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Order")
    date_time = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=100, choices=order_status, default="pending")

    def __str__(self):
        return f'{self.id} {self.user} {self.status}'
    
class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.order.id} {self.order.status} {self.price}'
    