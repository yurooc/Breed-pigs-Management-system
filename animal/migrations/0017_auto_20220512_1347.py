# Generated by Django 3.1 on 2022-05-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0016_auto_20220505_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zhongzhu',
            name='qiandai',
        ),
        migrations.AddField(
            model_name='zhongzhu',
            name='houdai',
            field=models.CharField(default=0, max_length=255, verbose_name='后代种猪编号'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='caishi',
            field=models.CharField(choices=[('优', '优'), ('良好', '良好'), ('异常', '异常')], max_length=255, verbose_name='采食'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='jingye',
            field=models.CharField(choices=[('优', '优'), ('良', '良'), ('异常', '异常'), ('无', '无')], max_length=255, verbose_name='精液质量'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='peizhong',
            field=models.CharField(choices=[('是', '是'), ('否', '否')], max_length=255, verbose_name='是否已经配种'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='xiwei',
            field=models.CharField(choices=[('无异常', '无异常'), ('跛足', '跛足'), ('惊厥', '惊厥'), ('攻击', '攻击'), ('爬跨', '爬跨')], max_length=255, verbose_name='行为'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='yimiao',
            field=models.CharField(choices=[('是', '是'), ('否', '否')], max_length=255, verbose_name='是否疫苗免疫'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='zaizhu',
            field=models.CharField(choices=[('是', '是'), ('否', '否')], max_length=255, verbose_name='是否为仔猪'),
        ),
        migrations.AlterField(
            model_name='zhongzhu',
            name='zhushe',
            field=models.IntegerField(default=1, verbose_name='猪舍'),
        ),
    ]