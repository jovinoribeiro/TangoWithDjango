# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0002_bookmark_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='summary',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
