# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-18 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(max_length=100)),
                ('ami_name', models.CharField(blank=True, max_length=100, null=True)),
                ('instance_id', models.CharField(max_length=100, unique=True)),
                ('hostname', models.CharField(max_length=100)),
                ('instance_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('cpu_core_num', models.IntegerField()),
                ('mem_total', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='assets',
            name='flavor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flavor', to='assets.Flavor'),
        ),
    ]
