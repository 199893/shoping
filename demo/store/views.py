from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

#首页
def index(request):
    return render(request,'store/index.html')

#登录
def login(request):
    return render(request,'store/login.html')

#注册
def signup(reqyest):
    return render(reqyest,'store/signup.html')

#优惠界面
def offers(request):
    return render(request,'store/offers.html')