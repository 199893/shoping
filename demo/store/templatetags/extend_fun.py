from django import template
from ..models import Classification
register = template.Library()


@register.simple_tag
def getcategorys():
    """
    返回分类
    :return:
    """
    # print(Classification.objects.all())
    return Classification.objects.all()

