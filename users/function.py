from utils.wrapper import *
from .models import *
from django.core.urlresolvers import reverse
import re


# 注册验证
def check_register_parms(request):
    user_name = post(request, 'user_name')
    user_pass1 = post(request, 'user_pwd')
    user_pass2 = post(request, 'user_cpwd')
    user_email = post(request, 'user_email')
    flag = True

    # 验证注册
    if not (5 < len(user_name) < 20):
        add_message(request, 'user_name', '用户名长度不对')
        flag = False

    if not (8 < len(user_pass1) < 20):
        add_message(request, 'user_pass', '用户名密码不对')
        flag = False

    if user_pass1 != user_pass2:
        flag = False
        add_message(request, 'user_pass2', '两次密码不一样')

    # 邮箱验证
    reg = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(reg, user_email):
        flag = False
        add_message(request, 'user_email', '用户名邮箱不对')

    # 判断名字是否存在
    if User.objects.get_by_name(user_name):
        add_message(request, 'user_name', '用户名已经存在，请不要重复注册')

        flag = False

    return flag


# 验证用户是否存在
def name_is_exist(request):
    user_name = get(request, 'user_name')
    return User.objects.get_by_name(user_name)


def check_login(request):
    """登录验证"""
    user_name = post(request, 'user_name')
    user_pass = post(request, 'user_pass')
    if not (5 < len(user_name) < 20):
        return False

    if not (8 < len(user_pass) < 20):
        return False

    user = User.objects.get_by_name(user_name)
    if not user:
        return False

    if not encryption_password(user_pass) == user.user_password:
        return False
    # from django.core.mail import send_mail



        # """
        # subject 主题
        # message 邮件文本内容
        # from_email 发送者
        # recipient_list 收件人列表
        # auth_user 邮箱服务器认证用户
        # auth_password 认证密码
        # html_message html邮件内容
        # def send_mail(subject, message, from_email, recipient_list,
        #           fail_silently=False, auth_user=None, auth_password=None,
        #           connection=None, html_message=None):
        # """
        #
    # content = '<a href="">请点击激活邮件!</a>'
    #
    # send_mail(subject='注册激活邮件',
    #
    #             message=content,
    #             from_email='Lit_leaf@163.com',
    #             recipient_list=['624526404@qq.com'],
    #             )
        # return HttpResponse('ok!')
    # return render(request, 'users/email.html', locals())
    return True


def keep_user_online(request):
    """保持登录状态"""
    user = User.objects.get_by_name(post(request, 'user_name'))
    set_session(request, 'user_name', user.user_name)
    set_session(request, 'uid', user.id)



def rem_username(request, response):
    if post(request, 'user_name'):
        # 将用户名写入cookie
        set_cookie(response, 'user_name', post(request, 'user_name'))


def get_pre_url(request):
    pre_url = get_cookie(request, 'pre_url')
    if not pre_url:
        pre_url = reverse('users:index')
    print('pre_url', pre_url)
    return pre_url


def check_address_info(request):
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    user_tele = post(request, 'user_tel')

    if len(user_recv) == 0:
        return False

    if len(user_addr) == 0:
        return False

    if len(user_code) != 6:
        return False

    if len(user_tele) != 11:
        return False

    return True
