# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20170703_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='place',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
