from django.shortcuts import render

# Create your views here.
import math
from datetime import datetime
from rest_framework.views import APIView
from common import success, fail, encrypt_password
from menu.models import RoleMenu, Menu
from role.models import UserRole
from role.serializers import UserRoleSerializer
from .serializers import UserSerializer
from .models import User, Picture
import secrets


# 用户注册
class AddUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        # print(data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            existing_user = User.objects.filter(username=username).first()
            if existing_user:
                return fail("账号已存在，请重新注册！")
            password = serializer.validated_data['password']
            password = encrypt_password(password)
            serializer.validated_data['password'] = password
            serializer.save()
            return success("请求成功")
        else:
            return fail("请求失败")


# 用户登陆
class Login(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")
        password = encrypt_password(password)
        user = User.objects.filter(username=username).first()
        user_password = User.objects.filter(password=password).first()
        if not (user and user_password):
            return fail("用户名或密码错误！")
        token = secrets.token_hex(64)
        user.token = 'eyJ'+token  # 关联token和用户
        user.update_time = datetime.now()
        user.save()  # 保存token到用户记录中
        access_token = {
            'token': 'eyJ'+token
        }

        return success(access_token)


# 退出登陆
class Logout(APIView):
    def post(self, request):
        uid = request.uid
        try:
            user = User.objects.get(id=uid)
            user.token = None  # 设置token为None
            user.save()
            return success("用户已退出登录")
        except User.DoesNotExist:
            return fail("找不到该用户")


# 获取当前登陆用户信息
class CurrentUser(APIView):
    def post(self, request):
        uid = request.uid
        user = User.objects.get(id=uid)
        serializer = UserSerializer(user)
        return success(serializer.data)


# 用户删除
class DeleteUser(APIView):
    def post(self, request):
        print(request.data)
        user = User.objects.filter(id=request.data['id']).first()
        if user:
            user.delete()
            return success("删除成功")
        else:
            return fail("用户不存在")


# 用户修改
class UpdateUser(APIView):
    def post(self, request):
        print(request.data)
        user_id = request.data['id']
        user = User.objects.filter(id=user_id).first()
        if user:
            data = request.data
            serializer = UserSerializer(instance=user, data=data)
            if serializer.is_valid():
                username = serializer.validated_data.get('username', user.username)
                existing_user = User.objects.filter(username=username).exclude(id=user_id).first()
                if existing_user:
                    return fail("用户名已存在，请重新输入！")
                password = serializer.validated_data.get('password', user.password)
                password = encrypt_password(password)
                serializer.validated_data['password'] = password
                serializer.save()

                return success("用户信息修改成功")
            else:
                return fail(serializer.errors)
        else:
            return fail("用户不存在")


# 根据id查询用户
class GetUserById(APIView):
    def post(self, request):
        user_id = request.data['id']
        try:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return success(serializer.data)
        except User.DoesNotExist:
            return fail("用户不存在")


# 查询所有用户
class GetAllUsers(APIView):
    def post(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return success(serializer.data)


# 分页获取用户信息
class GetUserPageList(APIView):
    def post(self, request):
        page = int(request.data.get('page', 1))  # get the current page number, default is 1
        size = int(request.data.get('size', 10))  # get the number of items per page, default is 10
        key = request.data.get('key', '')  # get the search keyword

        users = User.objects.filter(username__contains=key)  # filter users based on the search keyword
        total_count = users.count()  # total number of users

        # Calculate the number of pages
        total_pages = math.ceil(total_count / size)

        # Calculate the starting and ending indices of users to retrieve based on the current page
        start_index = (page - 1) * size
        end_index = start_index + size

        # Retrieve the users for the current page
        users_page = users[start_index:end_index]

        # Serialize the users
        serializer = UserSerializer(users_page, many=True)

        # Prepare the response data
        data = {
            'total_count': total_count,
            'total_pages': total_pages,
            'current_page': page,
            'per_page': size,
            'users': serializer.data
        }

        return success(data=data)


# 用户添加角色
class UserAddRole(APIView):
    def post(self, request):
        data = request.data
        user_role = UserRole.objects.filter(user_id=data["user_id"], role_id=data["role_id"]).first()
        if user_role is not None:
            return fail("请勿重复分配角色")
        serializer = UserRoleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return success("角色分配成功")
        return fail(serializer.errors)


# 用户删除角色
class UserDeleteRole(APIView):
    def post(self, request):
        data = request.data
        user_role = UserRole.objects.filter(user_id=data["user_id"], role_id=data["role_id"]).first()
        # role_menu_models = RoleMenu.objects.filter(role_id=data["role_id"])
        if user_role is None:
            return fail("该用户已经不存在该角色")
        user_role.delete()
        return success("角色移除成功")


# 获取用户角色列表
class UserRoleIdList(APIView):
    def post(self, request):
        user_id = request.data['user_id']
        user_role_models = UserRole.objects.filter(user_id=user_id)
        role_id_list = [model.role_id for model in user_role_models]
        return success(role_id_list)


# 获取登陆用户树结构菜单列表
class UserRoute(APIView):
    def post(self, request):
        uid = request.uid
        to_array = User.get_user_route(uid)
        result = []

        # Get all parent nodes
        arr = [value for value in to_array if value.parent_id == 0]

        for value in arr:
            arr1 = {
                "menu_id": value.menu_id,
                "path": value.path,
                "component": value.component,
                "label": value.label,
                "icon": value.icon,
                "redirect": value.redirect,
                "name": value.name,
                "parent_id": value.parent_id,
                "hidden": value.hidden,
                "order_num": value.order_num,
                "remark": value.remark,
                "children": Menu.set_children(value.menu_id, to_array)
            }
            result.append(arr1)

        return success(result)
