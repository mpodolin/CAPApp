# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150903_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 4, 1, 34, 24, 677898, tzinfo=utc), blank=True),
        ),
    ]
