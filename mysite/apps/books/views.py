from django.http import HttpResponse


def index(request):
    return HttpResponse('hello')


def test(request):
    return HttpResponse('test')
