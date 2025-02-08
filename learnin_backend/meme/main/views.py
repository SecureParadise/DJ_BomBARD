from django.shortcuts import render
# 
from django.http import HttpResponse
from .utils import *
# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

def register(request):
    name = request.GET.get('name')
    if name != None:
        return render(request, 'register.html',{'name':name})
    return render(request, 'register.html')

def vharti(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        contact = request.POST['contact']
        userData = {
            'name':name,
            'contact':contact,
            'email':email,
            'password':password
        }
        # Register User
        response = registerUser(userData) 
        # print("This is post on console event")
        # return HttpResponse(f"A POST request was amde. Email")   
        # return HttpResponse(f"A POST request was amde. Email:{email} ,Password{password} ,Gender{gender}")
        return render(request,"register.html",{'message':"Successfuly received"})  
    elif request.method == "GET":
        return HttpResponse("A GET request")
    else:
        return HttpResponse("<h1 bgcolor='grey'>Invalid Manushya</h1>")