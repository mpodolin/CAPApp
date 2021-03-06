# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150902_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 2, 23, 33, 30, 308614, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, default='Weekly Meeting'),
        ),
    ]
