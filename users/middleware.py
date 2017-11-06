from django.core.urlresolvers import reverse
from utils.wrapper import *
from django.utils import deprecation


class RecordUrlMiddleWare(deprecation.MiddlewareMixin):
    print('中间件')
    def process_response(self, request, response):
        urls = [
            reverse('users:login'),
            reverse('users:login_handle'),
            reverse('users:register'),
            reverse('users:register_handle'),
            reverse('users:check_user_name'),
            reverse('users:index'),
            reverse('users:order'),
            reverse('users:address'),
            # reverse('goods:index'),
            reverse('users:logout'),

        ]
        print('request.path',request.path)
        if request.path not in urls and response.status_code == 200:
            set_cookie(response, 'pre_url', request.get_full_path())
            print('---')
        return response
