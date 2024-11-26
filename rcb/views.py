from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Kohli(request):
    return HttpResponse('<h1>Kohli is the captain of RCB</h1>')
