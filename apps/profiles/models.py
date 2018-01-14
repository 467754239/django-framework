# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('0', u'无'),
        ('1', u'总监'),
        ('2', u'经理'),
        ('3', u'研发'),
    )
    user    = models.OneToOneField(User, primary_key=True)
    phone   = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'电话号码')
    role    = models.CharField(max_length=1, default='0', blank=True, choices=GENDER_CHOICES, verbose_name=u'角色')

    def __unicode__(self):
        return u'{0}-{1}'.format(self.user, self.phone)

    @property
    def todict(self):
        exclude = ['id']
        return { attr.name: getattr(self, attr.name) for attr in self._meta.fields if attr.name not in exclude }


@receiver(post_save, sender=User)
def create_save_user(sender, **kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if instance.is_superuser:
        return True

    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
