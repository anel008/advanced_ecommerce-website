from django.urls import path
from  .import views


urlpatterns = [
     path('cartdetails',views.cart_details, name = 'cartdetails'),
     path('addcart/<int:product_id>/', views.add_cart, name = 'addcart'),
]
