from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.


class Product(models.Model):

    product_name = models.CharField(max_length=100,unique=True)
    category     = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug         = models.SlugField(max_length=120,unique=True)
    description  = models.TextField(max_length=150)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photos/product')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug ,self.slug])

