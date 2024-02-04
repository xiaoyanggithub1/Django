from user.models import User
from common import success, fail
from datetime import datetime, timedelta
from pytz import timezone


class TokenAuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path != '/user/login/':  # 过滤掉登录接口
            # token = request.headers.get('Authorization', '').split(' ')[-1]  # 获取token
            token = request.headers.get('token', '').split(' ')[-1]  # 获取token
            if token:
                user = User.objects.filter(token=token).first()
                # print(user)
                if user:
                    now = datetime.now()
                    # if user.update_time + timedelta(days=7) >= now:
                    if 1 == 1:
                        request.uid = user.id  # 将用户对象赋值给request.user
                        response = self.get_response(request)
                        # 添加CORS头
                        response["Access-Control-Allow-Origin"] = "*"
                        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
                        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
                        response["Access-Control-Allow-Credentials"] = "true"
                        return response
                    else:
                        return fail('登录失效')
                else:
                    return fail('登录失效')
            else:
                return fail('登录失效')

        response = self.get_response(request)
        return response
