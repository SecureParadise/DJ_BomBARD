from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("Hello World, about")

def contact(request):
    return HttpResponse("Hello World,COntact")
 