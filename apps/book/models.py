# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import datetime

from django.db import models
from django.utils import timezone


# Create your models here.


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


class BaseModel(models.Model):
    name        = models.CharField(max_length=32)
    create_time = models.DateField(null=True, blank=True, auto_now_add=True)
    update_time = models.DateField(null=True, blank=True, auto_now=True)
    #create_time = models.DateField(default=timezone.now)
    #update_time = models.DateField(default=timezone.now)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        abstract = True


class Publish(BaseModel):
    city        = models.CharField(max_length=32)


class Book(BaseModel):
    price       = models.IntegerField()
    publish     = models.ForeignKey("Publish")


class School(models.Model):
    name    = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    phone   = models.CharField(max_length=32)
