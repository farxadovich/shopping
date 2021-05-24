
from django.shortcuts import  HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'shopp/home.html')

def index(request):
    return render(request, 'shopp/index.html')




