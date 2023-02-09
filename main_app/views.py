from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Home view
def home(request):
    return HttpResponse('<h1>Hello<h1>') 