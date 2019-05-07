from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


# 首页
def index(request):
    return render(request,'store/index.html')


# 登录
def login(request):
    return render(request,'store/login.html')


# 注册
def signup(reqyest):
    return render(reqyest,'store/signup.html')


# 优惠界面
def offers(request):
    return render(request,'store/offers.html')


# 关于我们
def about(request):
    return render(request, 'store/about.html')


# 市井
def marketplace(request):
    return render(request, 'store/marketplace.html')


# 核心价值
def values(request):
    return render(request, 'store/values.html')


# 隐私政策
def privacy(request):
    return render(request, 'store/privacy.html')
