from django.db import models


class Block(models.Model):
    id = models.AutoField(primary_key=True)
    index = models.IntegerField(null=True, blank=True)
    proof = models.IntegerField(null=True, blank=True)
    student_id = models.IntegerField(null=True, blank=True)
    time_stamp = models.CharField(max_length=255, null=True, blank=True)
    data = models.CharField(max_length=255, null=True, blank=True)
    data_hash = models.CharField(max_length=255, null=True, blank=True)
    trade = models.CharField(max_length=255, null=True, blank=True)
    pre_hash = models.CharField(max_length=255, null=True, blank=True)
    self_hash = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'block'
