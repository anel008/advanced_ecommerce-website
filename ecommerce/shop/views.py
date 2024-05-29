from django.shortcuts import render,get_object_or_404,Http404
from .models import Categ,Products

# Create your views here.
def home(request,c_slug = None):
    c_page = None
    prodt = None
    if c_slug != None :
        c_page =get_object_or_404(Categ,slug = c_slug)
        prodt = Products.objects.filter(category = c_page,available = True)
    else :
        prodt = Products.objects.all().filter(available = True)
    cat = Categ.objects.all()
    return render(request,'index.html',{'product' : prodt, 'ct':cat})


def product_item(request,c_slug,product_slug):
    try:
        prod = Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render (request,'items.html',{'pr':prod})

