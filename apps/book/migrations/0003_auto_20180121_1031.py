# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-21 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180121_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='update_time',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='update_time',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
