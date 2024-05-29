from django.shortcuts import render,get_object_or_404,Http404
from .models import Categ,Products
from django.db.models import Q

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

def search(request):
    prodt = None
    query = None
    if 'q' in request.GET :
        query = request.GET.get('q')
        prodt = Products.objects.all().filter(Q(name__contains= query)|Q(desc__contains = query)) 
    return render(request,'search.html',{'product':prodt, 'qr':query})