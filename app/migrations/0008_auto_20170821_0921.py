# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170821_0908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnelprofile',
            name='is_own_house',
        ),
        migrations.AddField(
            model_name='personnelprofile',
            name='own_house',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
