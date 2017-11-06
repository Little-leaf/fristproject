from django.template import Library

register = Library()


@register.filter
def browse_sort(new_list):
    goods_list = list()
    for good in new_list:
        goods_list.append(good)
    goods_list.sort(key=lambda obj: obj.set_time, reverse=True)
    # my_goods.sort(key=lambda obj: obj.update_time, reverse=True)

    return goods_list