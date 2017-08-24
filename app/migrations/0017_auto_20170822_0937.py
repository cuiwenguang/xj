# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20170822_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnelmigration',
            name='inflow_address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personnelmigration',
            name='inflow_date',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personnelmigration',
            name='outflow_address',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personnelmigration',
            name='outflow_date',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='personnelprofile',
            name='native_place',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]