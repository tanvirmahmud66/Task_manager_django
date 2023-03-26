from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def fahim(request):
    return HttpResponse("Hello Fahim!")

def tanvir(request):
    return HttpResponse("Hello Tanvir!")

def greeting(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")

def index(request):
    return render(request, 'hello/index.html')