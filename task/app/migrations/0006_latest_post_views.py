# Generated by Django 2.0 on 2018-01-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180108_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='latest_post',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
