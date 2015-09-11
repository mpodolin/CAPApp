# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadet',
            name='timetest',
            field=models.TimeField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='cadet',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
        migrations.AlterField(
            model_name='cadet',
            name='date_of_rank',
            field=models.DateField(default=django.utils.timezone.now, blank=True),
        ),
    ]
