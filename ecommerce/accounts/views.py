from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request,'register.html')

def registerin(request):
    if request.method == 'POST' :
        user_name = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2 :
            messages.info(request,"password don't match")
            return render(request,'register.html')
        elif User.objects.filter(username = user_name).exists():
            messages.info(request,"username taken")
            return render(request,'register.html')
        else:
            user = User.objects.create_user(username=user_name,password=password1,first_name=firstname,last_name=lastname)
            user.save()
            print('user created')
            return render(request,'login.html')  
    else:
        return render(request,'register.html')
    



def login(request):
    if request.method == "POST":
        Username = request.POST['username']
        Password = request.POST['password']

        user = auth.authenticate(username=Username, password=Password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')
    else :
         return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')