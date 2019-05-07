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
def signup(request):
    return render(request,'store/signup.html')


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



















#网站地图
def sitemap(request):
    return render(request,'store/sitemap.html')


#帮助
def help(request):
    return render(request,'store/help.html')

# 联系我们
def contact(request):
    return render(request, 'store/contact.html')


# 常见问题
def faq(request):
    return render(request, 'store/faq.html')

#信用卡
def card(request):
    return render(request,'store/card.html')
	
#电子产品购物
def products(request):
    return render(request,'store/products.html')

