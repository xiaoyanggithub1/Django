from django.db import models


class MentalMessages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)  # 姓名
    sex = models.IntegerField(null=True)  # 性别
    age = models.IntegerField(null=True)  # 年龄
    class_name = models.CharField(max_length=255, null=True)  # 班级名称
    phone = models.CharField(max_length=255, null=True)  # 电话号码
    emotion = models.CharField(max_length=255, null=True)  # 情绪
    mind_score = models.IntegerField(null=True)  # 心理评分
    mind_issue = models.TextField(null=True)  # 心理问题
    mind_advice = models.TextField(null=True)  # 心理建议
    tutor_log = models.TextField(null=True)  # 辅导日志
    grade_time = models.DateTimeField(auto_now=True, null=True)  # 打分时间

    class Meta:
        managed = False
        db_table = 'student_mentalmessages'
