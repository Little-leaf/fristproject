from django.shortcuts import render
from utils.wrapper import *
from .function import *
from django.core.paginator import Paginator
from .models import *

@cart_goods_sum
def index(request):

    ad1 = Advert.objects.all()[:4]
    ad2 = Advert.objects.all()[4:]

    cags = Category.objects.all()
    for cag in cags:
        # 最新的４个商品
        new_goods = GoodInfo.objects.new_goods(cag)

        # 最火的商品
        hot_goods = GoodInfo.objects.hot_goods(cag)
        cag.new = new_goods
        cag.hot = hot_goods

    return render(request, 'goods/index.html', locals())


@cart_goods_sum
def list(request, cag_id, page_id):
    cags = Category.objects.all()
    # 获取分类的商品
    show = get(request, 'show')
    goods_list = GoodInfo.objects.goods_divide(cag_id, show)

    paginator = Paginator(goods_list, 10)
    goods_list = paginator.page(page_id)
    page_id = int(page_id)
    # 获取最新的两个商品
    new_goods = GoodInfo.objects.get_2_new_goods()
    return render(request, 'goods/list.html', locals())


@cart_goods_sum
def detail(request):
    """商品详情页"""
    cags = Category.objects.all()

    goods = GoodInfo.objects.get(pk=get(request, 'goods_id'))

    # 最新的两个商品
    new_goods = GoodInfo.objects.get_2_new_goods()

    # 更新用户浏览纪录
    update_user_browse(request)

    return render(request, 'goods/detail.html', locals())
