from django.urls import path
from .views import BlogListView
from . import views


urlpatterns = [
    path('',BlogListView.as_view(),name='home'),
    path('test/',views.ghar,name='ghar')
]