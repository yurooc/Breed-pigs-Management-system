# Generated by Django 3.0.8 on 2022-03-20 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0005_auto_20220320_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhongzhu',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
