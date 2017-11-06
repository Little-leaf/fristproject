from django.shortcuts import render
from utils.wrapper import *
from carts.models import *
from users.models import *
from .models import *
import time
import random
from django.http import JsonResponse


def index(request):
    print('index')
    ids = post_list(request, 'goods_id')

    # 拼接商品的id列表
    goods_list = ','.join(ids)
    print(ids)
    carts = Cart.objects.filter(cart_good_id__in=ids, cart_user_id=get_session(request, 'uid'))
    total = 0
    money = 0
    for cart in carts:
        # 单个商品的总价
        cart.single_money = cart.cart_amount*cart.cart_good.goods_price
        money += cart.single_money
        total += cart.cart_amount
    carts.total = total
    carts.money = money

    user = User.objects.get(id=get_session(request, 'uid'))
    return render(request, 'order/place_order.html', locals())


def order_handle(request):
    # 订单页面跳转
    goods_ids = get(request, 'goods_ids').split(',')
    print(goods_ids)
    # 获取商品的id列表，和付款方式
    pay = get(request, 'pay')
    user_id = get_session(request, 'uid')
    carts = Cart.objects.filter(cart_good_id__in=goods_ids, cart_user_id=get_session(request, 'uid'))

    user = User.objects.get(id=user_id)

    # 完善订单信息
    order = Order()
    order.order_addr = user.user_addr
    order.order_recv = user.user_recv
    order.order_pay = pay
    order.order_user = user
    order.order_code = str(user_id) + str(time.time()) + random.randint(1000, 9999)
    order.save()

    for cart in carts:
        detail = Detail()
        detail.detail_amount = cart.cart_amount
        detail.detail_name = cart.cart_good.goods_name
        detail.detail_price = cart.cart_good.goods_price
        detail.detail_img = cart.cart_good.goods_image
        detail.detail_unit = cart.cart_good.goods_unit
        detail.detail_goods = order
        detail.detail_goodsid = cart.cart_good
        detail.save()
    # 删除购物车
    carts.delete()


    return JsonResponse({'ret': 1})