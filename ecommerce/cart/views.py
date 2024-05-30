from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from shop.models import *
from .models import *


# Create your views here.

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id :
        ct_id = request.session.create()
    return ct_id


def cart_details(request, tot = 0,count = 0,cart_items = None):
    try :
        ct = CartList.objects.get(cart_id = c_id(request))
        cart_items = Items.objects.filter(cart=ct, active = True)
        for i in cart_items:
            tot += (i.prodt.price*i.quan) 
            count += i.quan
    except ObjectDoesNotExist :
        pass
    return render(request,'cart.html',{'cartitems': cart_items, 'total':tot, 'count':count})


def add_cart(request, product_id):
    prod = Products.objects.get(id = product_id)
    try: 
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist :
        ct = CartList.objects.create(cart_id = c_id(request))
        ct.save()
    try:
        c_items = Items.objects.get(prodt = prod,cart = ct)
        if c_items.quan < c_items.prodt.stock :
            c_items.quan += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(prodt = prod, quan = 1, cart = ct)
        c_items.save()
    return redirect('cartdetails')


def min_cart(request):
    pass


def cart_delete(request):
    pass

