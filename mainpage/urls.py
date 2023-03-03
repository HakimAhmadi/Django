from django.contrib import admin
from django.urls import path, include
from mainpage import views 

urlpatterns = [
    path('', views.index),
    path('musicPlayer', include('playerUi.urls')),
    path('restApi', include('restApi.urls')),
    path('instaClone', include('instaClone.urls')),
    path('w3Clone', include('w3Clone.urls')),
]