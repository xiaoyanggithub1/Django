from django.db import models

# Create your models here.
from django.db import models
from flask import Response

from menu.models import Menu, RoleMenu
from role.models import UserRole


class User(models.Model):
    id = models.AutoField(primary_key=True)  # 主键
    username = models.CharField(max_length=255)  # 用户账号
    password = models.CharField(max_length=255)  # 用户密码
    name = models.CharField(max_length=255, null=True)  # 昵称
    phone = models.CharField(max_length=255, null=True)  # 用户手机号
    age = models.IntegerField(null=True)  # 年龄
    gender = models.IntegerField(null=True)  # 0代表女1代表男
    email = models.CharField(max_length=255, null=True)  # 用户邮箱
    picture_path = models.CharField(max_length=255, null=True)  # 用户头像
    status = models.IntegerField(default=1)  # 状态
    del_flag = models.IntegerField(default=1)  # 软删除 0代表删除 1代表正常用户
    update_time = models.DateTimeField(auto_now=True, null=True)  # 更新时间
    create_time = models.DateTimeField(auto_now_add=True, null=True)  # 创建时间
    token = models.CharField(max_length=255, null=True)
    pho = models.CharField(max_length=255, null=True)

    class Meta:
        managed = True
        db_table = 'user'

    @classmethod
    def get_user_route(cls, user_id):
        # Get the user's role IDs
        role_ids = UserRole.objects.filter(user_id=user_id).values_list('role_id', flat=True)
        # Get the menu IDs for the user's roles
        menu_ids = RoleMenu.objects.filter(role_id__in=role_ids).values_list('menu_id', flat=True)
        # Retrieve the menus
        menus = Menu.objects.filter(menu_id__in=menu_ids)
        return menus


# 用户头像
class Picture:
    @classmethod
    def changeTmgToUse(cls, picture_path):
        pass
