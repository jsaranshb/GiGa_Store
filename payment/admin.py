from django.contrib import admin
from .models import PaymentDetails

class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'transaction_id']

admin.site.register(PaymentDetails, PaymentDetailsAdmin)
