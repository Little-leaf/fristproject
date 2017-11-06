from django.db import models
from db.AbstractModel import *


class Detail(AbstractModel):
    """订单详情类"""

    # 商品的单位    # 商品名称
    detail_name = models.CharField(max_length=50)
    # 商品价格
    detail_price = models.IntegerField()
    # 商品的数量
    detail_amount = models.IntegerField()
    # 商品的单位
    detail_unit = models.CharField(max_length=20)
    # 商品图片
    detail_img = models.ImageField()
    # 商品ID
    detail_goodsid = models.IntegerField()
    # 订单商品列表
    detail_goods = models.ForeignKey('Order')


class Order(AbstractModel):
    """订单类"""

    status = (
        (1, '待付款'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '已完成'),
    )

    pay = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝支付'),
        (4, '银联支付'),
    )
    # 邮编
    order_code = models.CharField(max_length=11)
    # 地址
    order_addr = models.CharField(max_length=50)
    # 收件人
    order_recv = models.CharField(max_length=10)
    # 订单状态
    order_status = models.SmallIntegerField(choices=status, default=1)
    # 付款方式
    order_pay = models.SmallIntegerField(choices=pay, default=1)
    # 订单的所属者
    order_user = models.ForeignKey('users.User')
