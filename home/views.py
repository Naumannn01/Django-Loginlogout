
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

def index(request):
     if  request.user.is_anonymous:
        return redirect("/login")
     return render(request,'index.html')

def loginUser(request):
   if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,'Credentials Invalid')
            return redirect("/login")   
        elif user is not None:
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

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('/signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('/signup')
            else:
                new_user= User.objects.create_user(username=username, email=email, password=pass1)
                new_user.save()
                user_login = auth.authenticate(username=username, password=pass1)
                auth.login(request, user_login)
                return redirect("/") 
        else:
            messages.info(request, 'Your password does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
