# 引入注册对象
from django.template import Library

register = Library()


@register.filter
def create_image_name(index):
    return 'images/banner0' + str(index) + '.jpg'


