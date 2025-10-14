from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','category','price','is_available','updated_at']
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)