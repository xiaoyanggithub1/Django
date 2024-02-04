from django.db import models

# Create your models here.
from django.db import models


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=255, null=True, default=None, db_column='path', verbose_name='请求路径')
    component = models.CharField(max_length=255, null=True, default=None, db_column='component', verbose_name='组件')
    redirect = models.CharField(max_length=255, null=True, default=None, db_column='redirect', verbose_name='重定向')
    name = models.CharField(max_length=255, null=True, default=None, db_column='name', verbose_name='名字')
    label = models.CharField(max_length=255, null=True, default=None, db_column='label', verbose_name='标题')
    icon = models.CharField(max_length=255, null=True, default=None, db_column='icon', verbose_name='图标')
    parent_id = models.IntegerField(db_column='parent_id', verbose_name='父节点id 根节点为0')
    status = models.IntegerField(default=1, db_column='status', verbose_name='启用状态 1启用 0禁用')
    perm = models.CharField(max_length=255, null=True, default=None, db_column='perm', verbose_name='权限标识符')
    hidden = models.IntegerField(null=True, default=None, db_column='hidden')
    menu_type = models.CharField(max_length=255, null=True, default=None, db_column='menu_type',
                                 verbose_name='m为菜单 f为按钮（接口）')
    order_num = models.IntegerField(null=True, default=None, db_column='order_num', verbose_name='排序')
    remark = models.CharField(max_length=255, null=True, default=None, db_column='remark', verbose_name='备注')
    create_time = models.DateTimeField(null=True, default=None, db_column='create_time')
    update_time = models.DateTimeField(null=True, default=None, db_column='update_time')

    class Meta:
        db_table = 'menu'

    @staticmethod
    def if_children(menu_id, to_array):
        return any(value.parent_id == menu_id for value in to_array)

    @staticmethod
    def set_children(menu_id, to_array):
        return [{
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
        } for value in to_array if value.parent_id == menu_id]


class RoleMenu(models.Model):
    role_id = models.IntegerField()
    menu_id = models.IntegerField()

    class Meta:
        db_table = 'role_menu'
        unique_together = (('role_id', 'menu_id'),)
