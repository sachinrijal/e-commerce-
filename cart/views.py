from django.shortcuts import redirect, render
from store.models import Product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id) # this will get the product 
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request)) # it checks the card id
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cartitem = CartItem.objects.get(product=product,cart=cart)
        cartitem.quantity += 1
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(
            product=product,
            cart = cart,
            quantity = 1

        )
        cartitem.save()

    return redirect('cart')





def cart(request,total=0 ,quantity=0 , cartitems=None):
    try :
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cartitems = CartItem.objects.filter(cart=cart,is_active=True)

        for cartitem in cartitems:
            total += cartitem.product.price * cartitem.quantity
            quantity += 1

    except  ObjectDoesNotExist :
        pass


    context = {
        'total':total,
        'quantity': quantity,
        'cartitems':cartitems
    }

    print(total,cartitem)
    return render(request,'cart/cart.html',context)