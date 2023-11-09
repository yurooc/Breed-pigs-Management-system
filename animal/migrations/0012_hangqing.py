# Generated by Django 3.1 on 2022-04-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0011_delete_hangqing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hangqing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shengfen', models.CharField(max_length=255, verbose_name='省份')),
                ('junjia', models.CharField(max_length=11, verbose_name='均价（元/公斤）')),
                ('zuori', models.CharField(max_length=255, verbose_name='较昨天')),
                ('quanguo', models.CharField(max_length=255, verbose_name='较全国')),
            ],
        ),
    ]