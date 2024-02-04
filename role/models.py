from django.db import models

# Create your models here.
from django.db import models


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=255, verbose_name='角色名称')
    cover = models.CharField(max_length=255, null=True, blank=True, verbose_name='角色图标')
    remark = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(default=1, verbose_name='状态')
    del_flag = models.IntegerField(default=1, verbose_name='软删除 0代表删除 1代表正常用户')
    updata_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'role'


class UserRole(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        db_table = 'user_role'
        unique_together = ('user_id', 'role_id')
