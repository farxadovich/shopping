from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),

    path('second/', views.second, name='second'),
    path('uch/', views.uch, name='uch'),
    path('tort/', views.tort, name='tort'),
    path('besh/', views.besh, name='besh'),

]