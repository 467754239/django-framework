# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-03 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180121_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
    ]
