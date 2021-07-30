from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    l="Rango say hey there partner! <a href='/rango/about/'>About</a >"
    return HttpResponse(l)
 
def about(request):
    l1="Rango sayas here is another method <a href='/rango/'>Index</a >"
    return HttpResponse(l1)