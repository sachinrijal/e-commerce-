from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id

# Create your views here.

def store(request):
    products = Product.objects.filter(is_available = True)
    products_count = Product.objects.all().count()
    context = {
        'products':products,
        'products_count':products_count
    }
    
    return render(request,'store.html',context)


def product_by_category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = Product.objects.filter(category=category,is_available = True)
    products_count = products.count()
    
    context = {
        'products':products,
        'products_count':products_count
    }
    

    return render(request,'store.html',context)


def product_detail(request,category_slug,product_slug):
    product = get_object_or_404(Product,category__slug= category_slug,slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=product).exists()
    
    
    context = {
        'product':product,
        'in_cart':in_cart
    }

    return render(request,'product-detail.html',context)

