from django.http import HttpResponse


def test_sos(request):
    return HttpResponse("<h3> hii nidhi </h3>" )