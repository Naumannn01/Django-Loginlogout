
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

def index(request):
     if  request.user.is_anonymous:
        return redirect("/login")
     return render(request,'index.html')

def loginUser(request):
   if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")   
        else:
            return render (request,'login.html')
   return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def createUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('conpass')
        # print(username,email,pass1)
        if pass1!=pass2:
            return HttpResponse("your passwords does not match")
        new_user=User.objects.create_user(username,email,pass1)
        new_user.save()
        return redirect('/login')
    return render(request,'signup.html')
