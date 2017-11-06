from django.contrib import messages
from django.shortcuts import redirect, reverse
import hashlib


# 封装函数
# get获取
def get(request, key):
    return request.GET.get(key, '').strip()


# post获取
def post(request, key):
    return request.POST.get(key, '').strip()


# post list
def post_list(request, key):
    return request.POST.getlist(key)


# 设置cookie
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获取cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除整条session
def del_session(request):
    request.session.flush()


# 设置message
def add_message(request, key, value):
    messages.add_message(request, messages.INFO, key + ':' + value)


# 获取message
def get_message(request):
    messs = messages.get_messages(request)
    info = dict()
    for mess in messs:
        content = str(mess).split(':')
        info[content[0]] = content[1]
    print(info)
    return info


# 密码加密
def encryption_password(password, salt=''):
    sha = hashlib.sha256()
    new_password = password + '@#$%^&*()' + salt + ')(*&^%'
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()


# 用户是否登录
def user_online(request):
    return get_session(request, 'user_name')


# 用户登录权限
def check_permission(views_func):

    def wrapper(request, *args, **kwargs):

        if user_online(request):
            return views_func(request, *args, **kwargs)
        else:
            return redirect(reverse('users:login'))

    return wrapper

