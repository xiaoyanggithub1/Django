from django.shortcuts import render

# Create your views here.
from role.models import UserRole
from .models import Menu, RoleMenu
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MenuSerializer, RoleMenuSerializer
from common import success, fail, encrypt_password


# 菜单添加
class AddMenu(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success('请求成功')
        return Response(serializer.errors, status=400)


# 菜单删除
class DeleteMenu(APIView):
    def post(self, request):
        try:
            menu_id = request.data['menu_id']
            menu = Menu.objects.get(menu_id=menu_id)
            menu.delete()
            return success('菜单删除成功')
        except Menu.DoesNotExist:
            return fail('菜单不存在')
        except Exception as e:
            return fail(str(e))


# 菜单更新
class UpdateMenu(APIView):
    def post(self, request):
        try:
            menu_id = request.data['menu_id']
            menu = Menu.objects.get(menu_id=menu_id)
            serializer = MenuSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return success('菜单更新成功')
            return Response(serializer.errors, status=400)
        except Menu.DoesNotExist:
            return fail('菜单不存在')
        except Exception as e:
            return fail(str(e))


# 根据menu_id查询菜单
class GetMenu(APIView):
    def post(self, request):
        try:
            menu_id = request.data['menu_id']
            menu = Menu.objects.get(menu_id=menu_id)
            serializer = MenuSerializer(menu)
            return success(serializer.data)
        except Menu.DoesNotExist:
            return fail('菜单不存在')
        except Exception as e:
            return fail(str(e))


# 给角色添加菜单
class RoleAddMenu(APIView):
    def post(self, request):
        data = request.data
        role_menu = RoleMenu.objects.filter(role_id=data["role_id"], menu_id=data["menu_id"]).first()
        if role_menu:
            return fail("请勿重复授权")
        serializer = RoleMenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        # role_menus = RoleMenu.objects.filter(menu_id=data["menu_id"]).values("role_id")
        # for role_menu in role_menus:
        #     user_roles = UserRole.objects.filter(role_id=role_menu["role_id"]).values("user_id")
        #     for user_role in user_roles:
        #         Menu.update_user_perm(user_role["user_id"])
        return success("角色权限分配成功")


# 删除角色的菜单
class RoleDeleteMenu(APIView):
    def post(self, request):
        data = request.data
        role_menu = RoleMenu.objects.filter(role_id=data["role_id"], menu_id=data["menu_id"]).first()
        role_menus = RoleMenu.objects.filter(menu_id=data["menu_id"]).values("role_id")
        if not role_menu:
            return fail("该角色已经没有此权限")

        role_menu.delete()
        # for role_menu in role_menus:
        #     user_roles = UserRoleModel.objects.filter(role_id=role_menu["role_id"]).values("user_id")
        #     for user_role in user_roles:
        #         MenuModel.update_user_perm(user_role["user_id"])

        return success("角色权限移除成功")


# 获取角色菜单列表
class GetRoleMenuIdList(APIView):
    def post(self, request):
        role_id = request.data["role_id"]
        role_menus = RoleMenu.objects.filter(role_id=role_id)
        menu_ids = [model.menu_id for model in role_menus]
        return success(menu_ids)


