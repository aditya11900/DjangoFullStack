from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, Django! at home')
    return render(request, 'index.html')

def about(request):
    return HttpResponse('Hello, Django! at about')

def contact(request):
    return HttpResponse('Hello, Django! at contact')