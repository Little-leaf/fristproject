from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index/$', views.index, name='index'),
    url(r'login/$', views.login, name='login'),
    url(r'register/$', views.register, name='register'),
    url(r'order/$', views.order, name='order'),
    url(r'address/$', views.address, name='address'),
    # url(r'/$', views.index, name='index'),
    # 注册页面跳转
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'check_user_name/$', views.check_user_name, name='check_user_name'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^address_handle/$', views.address_handle, name='address_handle'),
    # url(r'^email/$', views.email, name='email'),

]
