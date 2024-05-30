from .models import *
from .views import *

def count(request):
    count_item = 0
    if 'admin' in request.path :
        return{}
    else :
        try:
            ct = CartList.objects.filter(cart_id = c_id(request))
            cti =Items.objects.all().filter(cart = ct[:1])
            for c in cti :
                count_item += c.quan
        except CartList.DoesNotExist :
            count_item = 0
        return dict(itm=count_item)
            