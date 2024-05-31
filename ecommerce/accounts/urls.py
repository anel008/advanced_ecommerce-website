from django.urls import path
from .import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login, name='login'),
    path('registerin',views.registerin, name='registerin'),
    path('logout',views.logout,name = 'logout')
]