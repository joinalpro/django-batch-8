from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tass (request):
    return render(request,'blog.html')
def ai_help(request):
    return render(request,'linkbuilding.html')