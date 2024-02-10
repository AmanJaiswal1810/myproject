from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import Feature

# Create your views here.

def index(request):
    Features = Feature.objects.all()
    return render(request,'index.html',{'features' : Features})

def counter(request):
    posts = [1,2,3,4,'tim','cook', 'tan']
    return render(request, 'counter.html',{'posts':posts})
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']
        
        if Password2 == Password1:
            if User.objects.filter(email =email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username already exist')
                return redirect('register')
            else :
                user = User.objects.create_user(username=username, email=email, password=Password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password didn't matched")
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST' :
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username=Username, password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html',{'pk':pk})