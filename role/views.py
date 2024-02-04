from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from common import success, fail, encrypt_password
from .models import Role
from role.serializers import RoleSerializer


# 新增角色
class AddRole(APIView):
    def post(self, request):
        data = request.data
        role_model = Role.objects.filter(rolename=data["rolename"]).first()
        if role_model is not None:
            return fail('角色已存在')
        # if "cover" in data and data["cover"]:
        #     serializers.change_tmg_to_use(data["cover"])
        role_serializer = RoleSerializer(data=data)
        if role_serializer.is_valid():
            role_serializer.save()
            return success('请求成功')
        return fail(role_serializer.errors)


# 删除角色
class DeleteRole(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            role = Role.objects.get(id=pk)
            role.delete()
            return success('角色删除成功')
        except Role.DoesNotExist:
            return fail('角色不存在')


# 更新角色
class UpdateRole(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            role = Role.objects.get(id=pk)
            data = request.data
            role.rolename = data.get('rolename', role.rolename)
            role.cover = data.get('cover', role.cover)
            role.remark = data.get('remark', role.remark)
            role.save()
            return success('角色更新成功')
        except Role.DoesNotExist:
            return fail('角色不存在')


# 根据id查找角色
class GetRole(APIView):
    def post(self, request):
        try:
            pk = request.data["id"]
            role = Role.objects.get(id=pk)
            role_serializer = RoleSerializer(role)
            return success(role_serializer.data)
        except Role.DoesNotExist:
            return fail('角色不存在')


# 查找所有角色
class GetAllRoles(APIView):
    def post(self, request):
        roles = Role.objects.all()
        role_serializer = RoleSerializer(roles, many=True)
        return success(role_serializer.data)
