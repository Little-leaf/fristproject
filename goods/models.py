from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField


class Category(AbstractModel):
    cag_name = models.CharField(max_length=50)


class GoodInfoManger(models.Manager):
    # 最新的商品
    def new_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    # 最火的商品
    def hot_goods(self, cag):
        return self.filter(goods_cag=cag).order_by('-goods_visits')[:3]

    # 获得最新添加的两个商品
    def get_2_new_goods(self):
        return self.all().order_by('-id')[:2]

    def goods_divide(self, cag_id, show):
        if show == '':
            return self.filter(goods_cag_id=cag_id)

        elif show == 'price':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_price')

        elif show == 'hot':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_visits')


class GoodInfo(AbstractModel):
    #TODO 商品类
    goods_name = models.CharField(max_length=30)

    goods_price = models.DecimalField(max_digits=10, decimal_places=2)

    goods_image = models.ImageField()

    goods_visits = models.IntegerField(default=0)

    goods_short = models.CharField(max_length=1000)

    goods_desc = HTMLField()

    goods_units = models.CharField(max_length=20)

    goods_sales = models.IntegerField(default=0)

    goods_cag = models.ForeignKey(Category)

    objects = GoodInfoManger()


# 广告模型类
class Advert(AbstractModel):

    ad_name = models.CharField(max_length=50)

    ad_image = models.ImageField()

    ad_link = models.CharField(max_length=40)
