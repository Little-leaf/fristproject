from django.shortcuts import render, reverse, redirect
from utils.wrapper import *
from .function import *
from django.http import JsonResponse, HttpResponse


@check_permission
def index(request):
    user = User.objects.get_by_name(get_session(request, 'user_name'))
    return render(request, 'users/user_center_info.html', locals())


def login(request):


    return render(request, 'users/login.html', locals())


def register(request):
    mess = get_message(request)
    return render(request, 'users/register.html', locals())


@check_permission
def address(request):
    user = User.objects.get_by_name(get_session(request, 'user_name'))

    return render(request, 'users/user_center_site.html', locals())


@check_permission
def order(request):
    return render(request, 'users/user_center_order.html', locals())


def register_handle(request):
    """注册跳转页面"""
    # 验证注册信息
    if check_register_parms(request):

        # return HttpResponse('ok!')
        # 保存信息到数据库
        User.objects.save_info(request)
        return redirect(reverse('users:login'))
    else:
        return redirect(reverse('users:register'))


def check_user_name(request):
    """验证用户注册用户名"""
    if name_is_exist(request):
        print('用户名存在')
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})


def login_handle(request):
    """验证登录"""
    if check_login(request):
        content = '恭喜您登录成功'

        send_mail(subject='注册激活邮件',

                  message=content,
                  from_email='Lit_leaf@163.com',
                  recipient_list=['wengjian@itcast.cn'],
                  )

        # 保持登录状态
        keep_user_online(request)
        response = redirect(get_pre_url(request))
        # 是否纪录用户名
        rem_username(request, response)
        return response

    else:
        return redirect(reverse('users:login'))


def logout(request):
    """注销"""
    url = get_pre_url(request)
    del_session(request)
    return redirect(url)


def address_handle(request):
    """修改用户收件地址"""
    if check_address_info(request):
        # 地址合法
        # 添加到数据库
        User.objects.save_address(request)
        return redirect(reverse('users:address'))



from django.core.mail import send_mail

# def email(request):
#
#     """
#     subject 主题
#     message 邮件文本内容
#     from_email 发送者
#     recipient_list 收件人列表
#     auth_user 邮箱服务器认证用户
#     auth_password 认证密码
#     html_message html邮件内容
#     def send_mail(subject, message, from_email, recipient_list,
#               fail_silently=False, auth_user=None, auth_password=None,
#               connection=None, html_message=None):
#     """

    # content = '<a href="">请点击激活邮件!</a>'
    #
    # send_mail(subject='注册激活邮件',
    #
    #           message=content,
    #           from_email='Lit_leaf@163.com',
    #           recipient_list=['624526404@qq.com'],
    #           )
    # return HttpResponse('ok!')
    # return render(request, 'users/email.html', locals())
#
#
# from __future__ import unicode_literals

# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
#
# subject = '来自自强学堂的问候'
#
# text_content = '这是一
    #
    # 封重要的邮件.'
#
# html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
#
# msg = EmailMultiAlternatives(subject, text_content, from_email, [to @ youemail.com])
#
# msg.attach_alternative(html_content, "text/html")
#
# msg.send()