from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'store/index.html')

def a(request):
    return render(request,'store/block.html')
