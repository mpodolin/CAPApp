# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0003_cadet_cadet_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadet',
            name='commander',
            field=models.BooleanField(default=False),
        ),
    ]
