# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0005_remove_bookmark_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 18, 39, 54, 800000), blank=True),
            preserve_default=True,
        ),
    ]
