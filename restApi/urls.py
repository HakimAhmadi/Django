from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('/item-detail', views.itemdetail),
    path('/aitem-detail/<int:pk>', views.aitemdetail),
    path('aitem-update/<int:pk>', views.aitemupdate),
    path('item-add', views.itemadd),
    path('item-delete/<int:pk>', views.itemdelete),
]
