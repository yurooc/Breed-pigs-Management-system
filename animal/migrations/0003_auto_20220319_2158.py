# Generated by Django 3.0.8 on 2022-03-19 21:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_zhongzhu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zhongzhu',
            options={'verbose_name': '种猪信息', 'verbose_name_plural': '种猪信息'},
        ),
        migrations.CreateModel(
            name='Yangzhiziliao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('neirong', models.TextField(verbose_name='内容')),
                ('creted_date', models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='记录提交时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
            ],
            options={
                'verbose_name': '养猪知识',
                'verbose_name_plural': '养猪知识',
            },
        ),
    ]
