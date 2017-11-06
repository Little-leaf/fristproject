from django.db import models

from db.AbstractModel import *


class CartManger(object):
    pass


class Cart(AbstractModel):
    """购物车类"""
    cart_good = models.ForeignKey('goods.GoodInfo')

    cart_user = models.ForeignKey('users.User')

    cart_amount = models.IntegerField(default=0)

    objects = CartManger()