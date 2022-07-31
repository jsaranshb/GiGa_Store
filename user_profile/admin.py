from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'mobile']
    search_fields = ['address']

admin.site.register(UserModel, UserModelAdmin)
