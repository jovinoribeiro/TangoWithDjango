# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leialater', '0006_bookmark_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileLeia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('to_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 24, 19, 25, 23, 10000), blank=True),
            preserve_default=True,
        ),
    ]
