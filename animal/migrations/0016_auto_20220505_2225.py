# Generated by Django 3.1 on 2022-05-05 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0015_auto_20220505_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhongzhu',
            name='peizhong',
            field=models.CharField(max_length=255, verbose_name='是否已经配种'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='pinzhong',
            field=models.CharField(choices=[('种公猪', '种公猪'), ('种母猪', '种母猪')], max_length=255, verbose_name='品种'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='qiandai',
            field=models.CharField(max_length=255, verbose_name='前代种猪编号'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='yimiao',
            field=models.CharField(max_length=255, verbose_name='是否疫苗免疫'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='zaizhu',
            field=models.CharField(max_length=255, verbose_name='是否为仔猪'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='zhushe',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='猪舍'),
        ),
    ]
