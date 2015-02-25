# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leialater', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='category',
            field=models.ForeignKey(default=1, to='leialater.Category'),
            preserve_default=False,
        ),
    ]
