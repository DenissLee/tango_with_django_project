from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    l="rango says hey there partner!"
    return HttpResponse(l)
 
