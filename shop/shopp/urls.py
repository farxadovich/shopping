from django.urls import path

from  . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('second/', views.second),
    path('uch/', views.uch, name='uch'),
    path('tort/', views.tort, name='tort'),
    path('besh/', views.besh, name='besh'),

]