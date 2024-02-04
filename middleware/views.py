from django.http import JsonResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from utils.jwt_auth import create_token


# 定义method_decorator 免 csrf校验， dispatch表示所有请求，因为所有请求都先经过dispatch
@method_decorator(csrf_exempt, name="dispatch")
class LoginView(View):
    """
    登陆校验
    """

    def post(self, request, *args, **kwargs):
        user = request.POST.get("username")
        pwd = request.POST.get("password")
        # 这里简单写一个账号密码
        if user == "xjk" and pwd == "123":
            # 登陆成功进行校验
            token = create_token({"username": "xjk"})
            # 返回JWT token
            return JsonResponse({"status": True, "token": token})
        return JsonResponse({"status": False, "error": "用户名密码错误"})


# 定义method_decorator 免 csrf校验， dispatch表示所有请求，因为所有请求都先经过dispatch
@method_decorator(csrf_exempt, name="dispatch")
class OrderView(View):
    """
    登陆后可以访问
    """

    def get(self, request, *args, **kwargs):
        # 打印用户jwt信息
        print(request.user_info)
        return JsonResponse({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user_info)
        return JsonResponse({'data': '删除订单'})
