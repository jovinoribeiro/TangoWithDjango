# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0004_bookmark_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='slug',
        ),
    ]
