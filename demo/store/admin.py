from django.contrib import admin
from .models import *
# Register your models here.


class User_admin(admin.ModelAdmin):
    """
    用户管理界面
    """
    #默认展示
    list_display = ['username','is_active','email']
    #分类
    list_filter = ['username','is_active']
    #默认搜索
    search_fields = ['username','email']
    #默认分页
    list_per_page = 10


class Classification_admin(admin.ModelAdmin):
    """
    商品分类管理
    """
    # 默认展示
    list_display = ['classname', 'date']
    # 分类
    list_filter = ['classname', 'date']
    # 默认搜索
    search_fields = ['classname']
    # 默认分页
    list_per_page = 10


class Commodity_admin(admin.ModelAdmin):
    """
    商品详细分类管理
    """
    # 默认展示
    list_display = ['cname', 'cclassification']
    # 分类
    list_filter = ['cname', 'cclassification']
    # 默认搜索
    search_fields = ['cname']
    # 默认分页
    list_per_page = 10

class Moregoods_admin(admin.ModelAdmin):
    """
    商品细致分类表
    """
    # 默认展示
    list_display = ['mcommodity', 'gcommodify']
    # 分类
    list_filter = ['mcommodity', 'gcommodify']
    # 默认搜索
    search_fields = ['mcommodity']
    # 默认分页
    list_per_page = 10


class Goods_admin(admin.ModelAdmin):
    """
    商品管理
    """
    # 默认展示
    list_display = ['goodsname', 'price','gmoregoods']
    # 分类
    list_filter = ['goodsname', 'gmoregoods']
    # 默认搜索
    search_fields = ['goodsname','price']
    # 默认分页
    list_per_page = 10


admin.site.register(User,User_admin)
admin.site.register(Moregoods,Moregoods_admin)
admin.site.register(Classification,Classification_admin)
admin.site.register(Commodity,Commodity_admin)
admin.site.register(Goods,Goods_admin)

