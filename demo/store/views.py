from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Classification,Commodity,Moregoods,Goods,Shoppingcart
#邮件发送模块
from django.core.mail import send_mail
from django.conf import settings
#邮件加密模块
from itsdangerous import TimedJSONWebSignatureSerializer as res,SignatureExpired


# Create your views here.


# 首页
def index(request):
    return render(request,'store/index.html')


# 登录
def login(request):
    if request.method=='GET':
        return render(request,'store/login.html')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            res= User.objects.filter(email=email)[0]
            if password == res.password and res.is_active==True:
                return HttpResponse('登录成功')
            elif password == res.password and res.is_active==False:
                return HttpResponse('账号未激活')
        except:
            return HttpResponse('账号不存在')


        return HttpResponse('密码错误')



# 注册
def signup(request):
    if request.method=='GET':
        return render(request,'store/signup.html')
    elif request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        user=User()
        try:
            if len(User.objects.filter(email=email)):
                return HttpResponse('邮箱已存在')
            else:
                if password==password2:
                    user.username=name
                    user.email=email
                    user.password=password
                    user.save()

                    id = User.objects.get(email=email).id
                    print(id)

                    serutil = res(settings.SECRET_KEY, 50)
                    resultid = serutil.dumps({'userid': id}).decode('utf-8')

                    send_mail("您需要点这封邮件激活商城品台账号", "<a href='http://127.0.0.1:8000/store/active/%s'> 点击此处激活</a>"%(resultid,), settings.DEFAULT_FROM_EMAIL, [email])

                    return render(request,'store/login.html')
                else:
                    return render(request,'store/signup.html')
        except:
            return HttpResponse('注册失败')


#邮件加密
def active(request,idstr):

    deser=res(settings.SECRET_KEY,50)
    try:
        obj=deser.loads(idstr)
        user=User.objects.get(pk=obj['userid'])
        user.is_active=True
        user.save()
        return redirect(reverse('store:login'))
    except SignatureExpired as e:
        return HttpResponse('链接已失效')


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

