from django.http import HttpResponse


def test():
    return HttpResponse('<h1> hello </h1> ')