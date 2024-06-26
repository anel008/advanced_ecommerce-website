from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_item, name='details'),
    path('search',views.search, name = 'search')
]
