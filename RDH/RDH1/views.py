from django.http import HttpResponse
from django.shortcuts import render
from RDH1.views import *

def home(request):
    return render(request,"home.html")