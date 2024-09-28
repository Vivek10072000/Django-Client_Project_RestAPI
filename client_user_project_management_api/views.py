from django.http import HttpResponse,request
from django.contrib.auth import logout
from django.shortcuts import render,redirect

def home(request):
    print("Home Page is requested")
    return render(request,'home.html')

def custome_logout(request):
    logout(request)
    return redirect("home")