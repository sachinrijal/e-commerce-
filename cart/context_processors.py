from .models import CartItem,Cart
from .views import _cart_id


def item_in_cart(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    
    try :
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cartitems = CartItem.objects.filter(cart=cart)

        for cartitem in cartitems:
            cart_count += cartitem.quantity

    except Cart.DoesNotExist:
        pass

    context = {
            'cart_count':cart_count
    }

    return dict(context)