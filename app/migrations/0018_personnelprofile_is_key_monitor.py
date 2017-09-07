# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20170822_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnelprofile',
            name='is_key_monitor',
            field=models.CharField(default=b'', max_length=50, null=True, blank=True),
        ),
    ]
