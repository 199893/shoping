from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import User,Classification,Commodity,Moregoods,Goods,Shoppingcart
#邮件发送模块
from django.core.mail import send_mail
from django.conf import settings
#邮件加密模块
from itsdangerous import TimedJSONWebSignatureSerializer as res,SignatureExpired
from django.contrib.auth.hashers import make_password, check_password
import random,re


# Create your views here.


# 首页
def index(request):

    

    if request.method=='GET':
        result = Goods.objects.all()
        #电子产品
        big = Classification.objects.all()
        a = []
        b = []
        c = []
        d = []
        e = []
        f =[]

        g=[]
        h=[]
        j=[]
        k=[]
        l=[]
        for i in big:
            if i.id==1:
                for qe in i.commodity_set.all():
                    for qs in qe.moregoods_set.all():
                        for ide in qs.goods_set.all():
                            b.append(ide)

            elif i.id == 2:
                for qe in i.commodity_set.all():
                    for qs in qe.moregoods_set.all():
                        for ide in qs.goods_set.all():
                            c.append(ide)
            elif i.id ==3:
                for qe in i.commodity_set.all():
                    for qs in qe.moregoods_set.all():
                        for ide in qs.goods_set.all():
                            d.append(ide)
            elif i.id==4:
                for qe in i.commodity_set.all():
                    for qs in qe.moregoods_set.all():
                        for ide in qs.goods_set.all():
                            e.append(ide)
            elif i.id==5:
                for qe in i.commodity_set.all():
                    for qs in qe.moregoods_set.all():
                        for ide in qs.goods_set.all():
                            f.append(ide)

        for i in range(7):

            q1 = random.choices(b)
            g.append(q1)
            if c != []:
                q2 = random.choices(c)
                h.append(q2[0])
            if d != []:
                q3 = random.choices(d)
                j.append(q3[0])
            if e != []:
                q4 = random.choices(e)
                k.append(q4[0])
            if f != []:
                q5 = random.choices(f)
                l.append(q5[0])

            qwe = random.choices(result)
            a.append(qwe[0])


        try:
            res=request.session.get('username')
            return render(request, 'store/index.html',{'username':res,'goods':a,'fashion':h,'child':j,'home':k,'sport':l})
            # return render(request, 'store/index.html',{'username':res,'goods':a})
        except:
            # return render(request, 'store/index.html',{'goods':a,})
            return render(request, 'store/index.html',{'goods':a,'fashion':h,'child':j,'home':k,'sport':l})



    elif request.method=='POST':
        search=request.POST['Search']
        if Moregoods.objects.filter(mcommodity=search):
            asd=Moregoods.objects.filter(mcommodity=search)[0].id

            return redirect(reverse('store:product',args=[asd,]))
            # return render(request,'')
        else:
            res = request.session.get('username')
            a = '请输入正确的类别'
            # return render(request, 'store/index.html', {'username': res, 'a': a})
            return redirect(reverse('store:index'),{'a':a})


# 登录
def login(request):
    if request.method=='GET':
        return render(request,'store/login.html')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            res= User.objects.filter(email=email)[0]


            if check_password(password,res.password)==True and res.is_active==True:

                request.session['username'] = res.username
                return redirect(reverse('store:index'))
            elif password == res.password and res.is_active==False:
                return HttpResponse('账号未激活')
        except:
            return HttpResponse('账号不存在')


        return HttpResponse('密码错误')


# 登出
def loginout(request):
    if request.method=="GET":
        del request.session['username']
    return redirect(reverse('store:index'))


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
                    user.password=make_password(password)
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
    res = request.session.get('username')
    return render(request,'store/offers.html', {'username': res})


# 关于我们
def about(request):
    res = request.session.get('username')
    return render(request, 'store/about.html', {"username": res})


# 市井
def marketplace(request):
    res = request.session.get('username')
    return render(request, 'store/marketplace.html', {"username": res})


# 核心价值
def values(request):
    res = request.session.get('username')
    return render(request, 'store/values.html', {"username": res})


# 隐私政策
def privacy(request):
    res = request.session.get('username')
    return render(request, 'store/privacy.html', {"username": res})


#网站地图
def sitemap(request):
    asd = Classification.objects.all()
    res = request.session.get('username')

    # return render(request,'store/sitemap.html', {"username": res,'class1':class1})

    return render(request,'store/sitemap.html', {"username": res,'big':asd})





#帮助
def help(request):
    res = request.session.get('username')
    return render(request,'store/help.html', {"username": res})

# 联系我们
def contact(request):
    res = request.session.get('username')
    return render(request, 'store/contact.html', {"username": res})


# 常见问题
def faq(request):
    res = request.session.get('username')
    return render(request, 'store/faq.html', {"username": res})

#信用卡
def card(request):
    res = request.session.get('username')
    return render(request,'store/card.html', {"username": res})
	
#电子产品购物
def products(request,id):
    cls=Commodity.objects.get(pk=id)
    cls1=cls.moregoods_set.all()
    a = []
    for i in cls1:
        for e in i.goods_set.all():
            print(e.discount,'++++++++++++++++')
            a.append(e)

    res = request.session.get('username')
    return render(request,'store/products.html', {"username": res,'cls':cls,'cls1':a})

def single(request,id):
    obj = Goods.objects.get(pk=id)
    # r =Moregoods.objects.get(pk=obj.gmoregoods)
    s = []
    ressa = obj.gmoregoods.gcommodify.moregoods_set.all()
    for aa in ressa:
        for aa2 in aa.goods_set.all():
            s.append(aa2)
    result = Goods.objects.all()
    a = []
    b=[]
    for i in range(7):
        qwe = random.choices(result)
        a.append(qwe[0])
        we = random.choices(s)
        b.append(we[0])
    print(b)
    res = request.session.get('username')
    return render(request,'store/single.html', {"username": res,"goodsid":obj,'goods':a,'more':b})

#查询所有小标签的商品
def product(request,id):
    res = request.session.get('username')
    goods = Moregoods.objects.get(pk=id)
    return render(request,'store/products.html', {"username": res,"goods":goods})

#搜索界面
def search(request):
    content = request.POST["content"]
    a = []
    b=[]
    asd = Goods.objects.all()
    res = Goods.objects.all().filter(goodsname__startswith=content)
    for i in asd:
        a.append(i)
    for q in res:
        b.append(q)

    if a != b:


        from django.core import serializers
        res = serializers.serialize('json',res)
        # print(res,type(res))


        return HttpResponse(res)
    else:
        return HttpResponse('')
