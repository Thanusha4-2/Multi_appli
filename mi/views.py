from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Mumbai(request):
    return HttpResponse('<h1>Mumbai Indians</h1>')