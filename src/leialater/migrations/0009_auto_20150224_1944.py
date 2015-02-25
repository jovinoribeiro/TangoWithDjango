# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0008_auto_20150224_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileleia',
            old_name='website',
            new_name='to_website',
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 19, 44, 15, 391000), blank=True),
            preserve_default=True,
        ),
    ]
