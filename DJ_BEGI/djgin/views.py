from django.http import *

def home(request):
    return HttpResponse("Hello , DjGin ! ")