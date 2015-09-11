# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150902_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 2, 23, 34, 4, 822981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
