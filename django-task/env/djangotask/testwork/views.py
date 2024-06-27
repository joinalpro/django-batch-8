from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def working (request):
    return HttpResponse("My name is Joinal Abden, I'm working.")