from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def store(request):
    products = Product.objects.filter(is_available = True).order_by('id')
    products_count = products.count()
    paginator = Paginator(products,2)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)
    context = {
        'products':paged_products,
        'products_count':products_count
    }
    
    return render(request,'store.html',context)


def product_by_category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = Product.objects.filter(category=category,is_available = True).order_by('id')
    products_count = products.count()
    paginator = Paginator(products,2)
    page_number = request.GET.get('page')
    paged_products = paginator.get_page(page_number)
    
    context = {
        'products':paged_products,
        'products_count':products_count,

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

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            products= Product.objects.filter(Q(product_name__icontains = keyword) | Q(description__icontains = keyword)).order_by('created_at')
            product_count = products.count()

    context = {
            'products':products,
            'products_count':product_count
    }

    return render(request,'store.html',context)

    


