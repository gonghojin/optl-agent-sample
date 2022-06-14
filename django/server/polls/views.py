from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def error(request):
    raise NotImplementedError
    return HttpResponse("Hello, world. You're at the polls index.")
