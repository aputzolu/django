# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20170703_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='name',
        ),
    ]
