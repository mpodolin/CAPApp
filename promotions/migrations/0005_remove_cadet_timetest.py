# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0004_cadet_commander'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='timetest',
        ),
    ]
