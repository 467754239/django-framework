# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Album(models.Model):
    album_name          = models.CharField(max_length=100)
    artist              = models.CharField(max_length=100)

    def __unicode__(self):
        return '<%s>' % self.album_name


class Track(models.Model):
    '''
        models.CASCADE: 默认的选项，当外键关联的字段删除的时候，所有其他表级联删除
        http://blog.csdn.net/orangleliu/article/details/40268495
    '''
    album               = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order               = models.IntegerField()
    title               = models.CharField(max_length=100)
    duration            = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')
        ordering        = ['order']

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)

