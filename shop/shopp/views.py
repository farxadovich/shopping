
from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/second/">Birinchi sayt</a>'
                        "<br><br><button>""<h5 style='text-shadow: 0 0 25px blue;'>"'<a href="//127.0.0.1:8000/second/">Next</a></button>')


def second(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/uch/">ikkinchi sayt</a>'
                        "<br><br><button>""<h5 style='text-shadow: 0 0 25px blue;'>"'<a href="//127.0.0.1:8000/uch/">Next</a></button>')



def uch(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/tort/">Uchinchi sayt</a>'
                        "<br><br><button>""<h5 style='text-shadow: 0 0 25px blue;'>"'<a href="//127.0.0.1:8000/tort/">Next</a></button>')



def tort(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/besh/">Tort sayt</a>'
                        "<br><br><button>""<h5 style='text-shadow: 0 0 25px blue;'>"'<a href="//127.0.0.1:8000/besh/">Next</a></button>')

def besh(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/">Besh sayt</a>'
                        "<br><br><button>""<h3 style='text-shadow: 0 0 25px blue;'>"'<a href="//127.0.0.1:8000/">HOME</a></button>')



