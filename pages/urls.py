from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getImage', views.getImage, name='getImage'),
    path('uploadImage', views.uploadImage, name='uploadImage'),

]