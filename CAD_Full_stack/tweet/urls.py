from django.contrib import admin
from django.urls import path
# for media handling
from django.conf import settings
from django.conf.urls.static import static
# import view
from . import views


urlpatterns = [
    path('', views.index,name='index_home'),
    path('tlist/', views.tweetlist,name='tweetlist'),
    path('tcreate/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.edit_tweet,name='edit_tweet'),
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 