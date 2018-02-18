# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Flavor(models.Model):
    name                        = models.CharField(max_length=32)
    cpu_core_num                = models.IntegerField()
    mem_total                   = models.DecimalField(max_digits=4, decimal_places=1)   # 最多为4位， 小数点后最多为1位。

    class Meta:
        db_table = 'flavor'

    def __unicode__(self):
        return '%s: %s-%s' % (self.name, self.cpu_core_num, self.mem_total)


class Assets(models.Model):
    ami_id                      = models.CharField(max_length=100)
    ami_name                    = models.CharField(max_length=100, null=True, blank=True)
    instance_id                 = models.CharField(max_length=100, unique=True)
    hostname                    = models.CharField(max_length=100)
    instance_name               = models.CharField(max_length=100)
    flavor                      = models.ForeignKey(Flavor, related_name='flavor', verbose_name="实例模板")
    remark                      = models.TextField(max_length=100, null=True, blank=True, verbose_name="备注")
    create_time                 = models.DateTimeField(auto_now_add=True)
    update_time                 = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'assets'

    def __unicode__(self):
        return self.instance_name


