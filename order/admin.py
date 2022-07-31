from django.contrib import admin
from .models import Order, OrderDetails 

class OrderDetailsInline(admin.TabularInline):
    model = OrderDetails
    extra = 0
    # To make inline model hide or show by using bootstrap classes ...
    #classes = ['collapse']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'user', 'status']
    search_fields = ['id']
    list_filter = ['status']
    inlines = [OrderDetailsInline]

admin.site.register(Order, OrderAdmin)

