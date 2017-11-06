from users.models import *
from utils.wrapper import *
from carts.models import *


def update_user_browse(request):
    """获得用户的浏览纪录"""

    # 判断用户是否登录
    if not user_online:
        return

    goods_id = get(request, 'goods_id')
    user_id = get_session(request, 'uid')
    limit = 5

    # 如果登录，判断浏览纪录是否有５条
    try:
        record = RecordBrowse.objects.get(browse_goods_id=goods_id, browse_user_id=user_id)
        record.save()

    # 没有５个，就添加
    except RecordBrowse.DoesNotExist:
        record = RecordBrowse.objects.filter(browse_user=user_id).order_by('set_time')
        if record.count() < limit:
            rd = RecordBrowse()
            rd.browse_goods_id = goods_id
            rd.browse_user_id = user_id
            rd.save()

        else:
        #５个，更新它的修改时间
            rd = record[0]
            rd.browse_goods_id = goods_id
            rd.save()


# 购物车商品数量显示，装饰器
def cart_goods_sum(view_func):
    def wrapper(request, *args, **kwargs):
        total = 0
        if user_online(request):
            carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))

            for cart in carts:
                total += cart.cart_amount
        request.total = total
        return view_func(request, *args, **kwargs)
    return wrapper


