from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['usrnm']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();
                print("user created")
            return redirect('/')
        else:
            # print("password not matched")
            messages.info(request,"password not matched")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['usrnm']
        password = request.POST['psw1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
