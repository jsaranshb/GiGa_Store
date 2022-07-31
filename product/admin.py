from itertools import product
from django.contrib import admin
from .models import Product, ProductCategory, ProductImages

# class ProductImageInline(admin.StackedInline):
#     model = ProductImages
#     extra = 0

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_category', 'price', 'status']
    search_fields = ['name']
    list_filter = ['status', 'product_category']
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    search_fields = ['name']
    list_filter = ['status']

admin.site.register(ProductCategory, ProductCategoryAdmin)




