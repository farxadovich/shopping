from django.http import HttpResponse


def index(request):
    return HttpResponse("<strong>Hello, world. You're at the polls index.<strong>")


def test(request):
    return HttpResponse("<a href='test/'>"
                            "<button>"
                                "<h1 style='text-shadow: 0 0 25px red;'>"
                                    "Hello, world. You're at the polls index."
                                "</h1>"
                            "</button>"
                        "</a>")