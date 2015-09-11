# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150902_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='squadron',
            field=models.CharField(max_length=6, default='MD-011'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 3, 1, 58, 48, 569465, tzinfo=utc)),
        ),
    ]
