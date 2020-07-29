

from django.shortcuts import render,redirect
from .models import Post,Maindata
from django.contrib.auth.models import User,auth
from django.contrib import messages
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

def interface4(request):
    #Query Data From Model
    data=Maindata.objects.all()
    return render(request,'page4maindata.html',{'mains':data})


def addUser(request):
    
    username=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']

    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username นี้มีคนใช้แล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email นี้มีคนใช้แล้ว')
            return redirect('/register')
        else :
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email

            )
            user.save()
            return redirect('/')
    else:
        messages.info(request,'รหัสผ่านไม่ตรงกัน')
        return redirect('/register')

def login(request):
    username=request.POST['username']
    password=request.POST['password']

    #login เช็ค username password ตรงกันมั้ย
    user=auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/page2')
    else :
        messages.info(request,'ไม่พบข้อมูลกรุณาสมัคร')
        return redirect('/register')

   
    
