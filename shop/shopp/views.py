
from django.shortcuts import  HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'shopp/home.html')

def index(request):
    return render(request, 'shopp/index.html')


def second(request):
    return render(request, 'shopp/second.html')



def uch(request):
    return render(request, 'shopp/uch.html')




def tort(request):
    return render(request, 'shopp/tort.html')

def besh(request):
    return render(request, 'shopp/besh.html')



