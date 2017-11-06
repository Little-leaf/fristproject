from django.db import models
from utils.wrapper import *
from db.AbstractModel import *


class User_Manger(models.Manager):
    """用户管理器"""
    def get_by_name(self, name):
        # 验证用户名是否存在
        try:
            return self.get(user_name=name)
        except:
            return None


    def save_info(self, request):
        user = User()

        user_name = post(request, 'user_name')
        user_pass = post(request, 'user_cpwd')
        user_pass = encryption_password(user_pass, '')
        user_email = post(request, 'user_email')

        user.user_name = user_name
        user.user_password = user_pass
        user.user_email = user_email

        user.save()

    def save_address(self, request):
        user = self.get_by_name(get_session(request, 'user_name'))
        user.user_recv = post(request, 'user_recv')
        user.user_addr = post(request, 'user_addr')
        user.user_code = post(request, 'user_code')
        user.user_tel = post(request, 'user_tel')
        user.save()




class User(AbstractModel):
    """用户类"""
    # 用户名
    user_name = models.CharField(max_length=50)
    # 用户密码
    user_password = models.CharField(max_length=64)
    # 用户邮箱
    user_email = models.CharField(max_length=100)
    # 用户地址
    user_addr = models.CharField(max_length=200)
    # 用户手机
    user_tel = models.CharField(max_length=11)
    # 编码
    user_code = models.CharField(max_length=6)
    # 收件人
    user_recv = models.CharField(max_length=30, default='')

    objects = User_Manger()

# 用户浏览记录模型
class RecordBrowse(AbstractModel):

    # 浏览商品
    browse_goods = models.ForeignKey('goods.GoodInfo')
    # 浏览者
    browse_user = models.ForeignKey('User')



