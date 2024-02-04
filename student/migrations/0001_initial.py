# Generated by Django 4.2.4 on 2023-12-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentalMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('sex', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('class_name', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('emotion', models.CharField(max_length=255, null=True)),
                ('mind_score', models.IntegerField(null=True)),
                ('mind_issue', models.TextField(null=True)),
                ('mind_advice', models.TextField(null=True)),
                ('tutor_log', models.TextField(null=True)),
                ('grade_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'mental_messages',
                'managed': False,
            },
        ),
    ]