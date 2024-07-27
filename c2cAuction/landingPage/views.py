from django.shortcuts import render

from django.http import HttpResponse , JsonResponse
# Create your views here.

def home(response):
    return render(response,'home.html')
    