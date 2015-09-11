# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150904_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 4, 1, 34, 44, 310334, tzinfo=utc), blank=True),
        ),
    ]
