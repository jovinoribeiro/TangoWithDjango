# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150220_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
