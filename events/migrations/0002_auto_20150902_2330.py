# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 2, 23, 30, 6, 110036, tzinfo=utc)),
        ),
    ]
