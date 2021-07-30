from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    l1="Rango say hey there partner! <a href='/rango/about/'>About</a >"
    return HttpResponse(l1)

def about(request):
    l2="Rango sayas here is another method <a href='/rango/'>Index</a >"
    return HttpResponse(l2)