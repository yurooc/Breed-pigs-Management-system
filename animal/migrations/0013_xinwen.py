# Generated by Django 3.1 on 2022-04-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0012_hangqing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xinwen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biaoti', models.CharField(max_length=255, verbose_name='新闻标题')),
                ('wenzhang', models.CharField(max_length=65536, verbose_name='新闻内容')),
            ],
        ),
    ]