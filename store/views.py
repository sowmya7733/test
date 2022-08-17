import email
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate #, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from Ecomerce_project import settings
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    return render(request , "Auth/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Confirm = request.POST['Confirm Password']
        mobile = request.POST['Mobile'] 
        Birth = request.POST['Birth']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('homepage')
        
        if User.objects.filter(email=Email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('homepage')

        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('homepage')
        
        if Password != Confirm :
            messages.error(request, "Passwords didn't matched!!")
            return redirect('homepage')
    
        myuser = User.objects.create_user(username , Email , Password )
        myuser.Firstname = Firstname
        myuser.LastName = Lastname
        myuser.Mobile =  mobile
        myuser.Birth = Birth
        myuser.save()

        messages.success(request,"Your Account has been Sucessfully created ")


        subject = "Welcome to Django Project"
        message = "Hello " + myuser.Firstname + "!! \n" + "Welcome to Django!! \n Thank you for visiting our website\n. We have sent you a confirmation email, please confirm your email address. \n\nThanking You\n Ecommerce Website"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [ myuser.email ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('login')

    else:
        return render(request,"Auth/signup.html") 

def login(request):

    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        # user = auth.authenticate(request,username=Username, Password=Password)
        user = authenticate(username=Username, password=Password)

        if user is not None:
            auth.login(request, user)
            # Firstname= user.Firstname
            return render(request,"Auth/index.html" ) # , {'Firstname':Firstname})
        else:
            # messages.error(request, "Bad Credentials")
            messages.info(request, "Enter correct details")
            return redirect('homepage')  # Changes Made
    else :
        return render(request,"Auth/Login.html") 

def logout(request):
    # logout(request, 'index.html')
    auth_logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("homepage")