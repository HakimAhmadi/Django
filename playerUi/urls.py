from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.main, name='main'),
    path('uploadpage', views.uploadpage, name='uploadpage'),
    path('uploadfile/', views.uploadfile, name='uploadfile'),
    path('uploadyt', views.uploadytpage, name='uploadytpage'),
    path('loadytfile', views.loadytfile, name='loadytfile'),
    path('downloadytfile', views.downloadytfile, name='downloadytfile'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
