from django.shortcuts import render
from utils.wrapper import *
from django.http import JsonResponse
from .models import *

@check_permission
def index(request):
    """购物车商品首页"""
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
    total = 0
    money = 0
    for cart in carts:
        # 单件商品的总价
        cart.single_money = cart.cart_amount * cart.cart_good.goods_price
        # 所有商品的数量
        total += cart.cart_amount
        # 所有商品的总价
        money += cart.single_money
    carts.total = total
    carts.money = money
    return render(request, 'carts/cart.html', locals())


@check_permission
def add_goods(request):
    # TODO
    # 首页
    # 获取goods_id
    goods_id = get(request, 'goods_id')
    # 获得uid
    uid = get_session(request, 'uid')
    # 获得商品数量
    goods_num = get(request, 'goods_num')
    print(goods_id)
    print(uid)
    print(goods_num)

    # 是否已经添加
    try:
        cart = Cart.objects.get(cart_good_id=goods_id, cart_user_id=uid)
        # 存在就更新商品的数量
        cart.cart_amount += int(goods_num)
        cart.save()

    # 不存在就添加
    except Cart.DoesNotExist:
        cart = Cart()
        cart.cart_good_id = goods_id
        cart.cart_user_id = uid
        cart.cart_amount = goods_num
        cart.save()

    # 统计购物车中的商品的数量
    carts = Cart.objects.filter(cart_user_id=uid)
    total = 0
    for cart in carts:
        total += cart.cart_amount

    return JsonResponse({'ret': total})


def edit_goods_num(request):
    id = get(request, 'id')
    num = get(request, 'num')
    print('id', id)
    print('num', num)
    try:
        cart = Cart.objects.get(cart_good_id=id, cart_user_id=get_session(request, 'uid'))
        cart.cart_amount = num
        cart.save()
    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1})


def remove_goods(request):
    # 删除商品
    id = get(request, 'id')
    try:
        cart = Cart.objects.get(cart_good_id=id, cart_user_id=get_session(request, 'uid'))
        print('cart', cart)
        cart.delete()
    except Cart.DoesNotExist:
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1})
