# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20150902_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadet',
            name='cadet_staff',
            field=models.BooleanField(default=False),
        ),
    ]
