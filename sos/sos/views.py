from django.http import HttpResponse

def test_sos(request):
    return HttpResponse("Hello, world. You're at the SOS test page.")