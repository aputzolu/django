# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 11:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20170704_0919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='company',
        ),
    ]
