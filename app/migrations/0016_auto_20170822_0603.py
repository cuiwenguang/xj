# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170822_0559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnelprofile',
            name='gender1',
        ),
        migrations.RemoveField(
            model_name='personnelprofile',
            name='is_minimum_security1',
        ),
        migrations.AlterField(
            model_name='personnelprofile',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personnelprofile',
            name='is_minimum_security',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
