# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from company.models import Company
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, null=True)
    def __unicode__(self):
        return self.user.username


# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile = UserProfile()
#         profile.user = instance
#         profile.save()

# post_save.connect(create_user_profile, sender=User)


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)