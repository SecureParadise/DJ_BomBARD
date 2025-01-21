from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    # Encountered heavy error due to type
    # templete = 'home.html'
    template_name = 'home.html'

def ghar(request):
    return render(request,'index.html')