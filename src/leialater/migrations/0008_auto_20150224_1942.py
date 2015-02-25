# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0007_auto_20150224_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 19, 42, 25, 653000), blank=True),
            preserve_default=True,
        ),
    ]
