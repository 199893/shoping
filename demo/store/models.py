from django.db import models

# Create your models here.


#用户表
class User(models.Model):
    """
    用户表，可以对用户的信息进行保存
    """
    #用户名
    username = models.CharField(max_length=20)
    #密码
    password = models.CharField(max_length=100)
    #邮件
    email = models.EmailField()
    # 金钱
    money = models.IntegerField(default=0)
    #激活
    is_active= models.BooleanField(default=False)
    #注册时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

#商品大分类表
class Classification(models.Model):
    """
    商品大分类表，可以对细分为多个商品分类
    """
    #商品分类名称
    classname = models.CharField(max_length=30)
    #分类创建时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classname

class Commodity(models.Model):
    """
    商品中分表，详细的分类出每个大分类的详细分类
    """
    #详细分类名称
    cname = models.CharField(max_length=30)
    #所属哪个分类
    cclassification = models.ForeignKey(Classification,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname


class Moregoods(models.Model):
    """
    所有分类，商品细分表，详细的分类出每个分类的详细分类
    """
    #分类名
    mcommodity = models.CharField(max_length=30)
    #分类数据外键
    gcommodify = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    #时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mcommodity

class Goods(models.Model):
    """
    商品表，详细的商品信息
    """
    #商品名称
    goodsname = models.CharField(max_length=30)
    #商品价格
    price = models.IntegerField(default=0)
    #商品折扣
    discount = models.FloatField(default=1)
    #商品简介
    description = models.CharField(max_length=100,default='')
    #商品描述
    descriptions = models.TextField(default='')
    # 商品增加时间
    date = models.DateTimeField(auto_now_add=True)
    #商品图片
    img = models.ImageField(upload_to='goodsimg')
    #所属分类
    gmoregoods = models.ForeignKey(Moregoods,on_delete=models.CASCADE)

    def __str__(self):
        return self.goodsname


class Shoppingcart(models.Model):
    """
    购物车
    """
    #用户id
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    #商品id
    goods_id = models.ForeignKey(Goods,on_delete=models.CASCADE)
    #添加时间
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """
    用户评论模块
    """
    #用户id
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    # 商品id
    goods_id = models.ForeignKey(Goods, on_delete=models.CASCADE)
    #评论内容
    content = models.TextField()

