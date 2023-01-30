from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login as LoginFunction

# Create your views here.

def home(r):
    return render(r,"landing.html")

def index(r):
    return render(r,"index.html")

def login(r):

    if r.method == "POST":
        username = r.POST.get('email')
        password = r.POST.get('password')
        user = authenticate(username = username,password = password)

        if user is not None:
            LoginFunction(r,user)
            return redirect(profile)
            

        else :
            return redirect (home)

    return render(r,"login.html")

def register(r):
    if r.method == "POST":
        u = User()
        u.first_name = r.POST.get('fname')
        u.last_name = r.POST.get('lname')
        u.email = r.POST.get('email')
        
        u.username = r.POST.get('username')
        u.set_password = (r.POST.get('password'))
        u.is_active = True
        u.is_staff = True
        u.save()

        a= Account()
        a.user = u
        a.gender= r.POST.get('gender')
        a.dob= r.POST.get('dob')
        a.contact= r.POST.get('contact')
        a.save()
        LoginFunction(r,u)
        return redirect (profile)


def profile(r):
    return render(r,"profile.html")

def logout(r):
    pass
