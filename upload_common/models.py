from django.db import models


class PictureModel(models.Model):
    path = models.CharField(max_length=255, verbose_name='图片路径')
    name = models.CharField(max_length=255, verbose_name='图片名称')
    size = models.CharField(max_length=255, verbose_name='图片大小')

    class Meta:
        db_table = 'picture'


class HomeIcon(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    class Meta:
        db_table = 'home_icon'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    apple = models.IntegerField()
    vivo = models.IntegerField()
    oppo = models.IntegerField()
    meizu = models.IntegerField()
    samsung = models.IntegerField()

    class Meta:
        db_table = 'orders'
