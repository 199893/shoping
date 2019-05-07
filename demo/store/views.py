from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'store/index.html')

def login(request):
    return render(request,'store/login.html')
