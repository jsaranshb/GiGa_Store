from django.db import models
from django.contrib.auth.models import User

class PaymentDetails(models.Model):

    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=80, null=True)
    transaction_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.payment_id
    