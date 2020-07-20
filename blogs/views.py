from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'page1.html')

def createForm(request):
    return render(request,'register.html')

def interface2(request):
    return render(request,'page2.html')

def interface3(request):
    #Query Data From Model
    data=Post.objects.all()
    return render(request,'page3querry.html',{'posts':data})

def addUser(request):
    
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    user=User.objects.create_user(
        password=password,
        username=username,
        email=email

        
        )
    user.save()
    return render(request,'register.html')

    
