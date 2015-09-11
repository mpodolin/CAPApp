# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('weekly_meeting', models.BooleanField(default=True)),
                ('activities', models.TextField(blank=True)),
                ('start', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 2, 23, 26, 46, 835310, tzinfo=utc))),
                ('uod_cadets', models.CharField(max_length=2, choices=[('PT', 'PT'), ('BD', 'BDU'), ('CA', 'Class A'), ('CB', 'Class B'), ('CC', 'Class C')], default='BD')),
                ('uod_staff', models.CharField(max_length=2, choices=[('PT', 'PT'), ('BD', 'BDU'), ('CA', 'Class A'), ('CB', 'Class B'), ('CC', 'Class C')], default='BD')),
                ('uod_senior', models.CharField(max_length=2, choices=[('PT', 'PT'), ('BD', 'BDU'), ('CA', 'Class A'), ('CB', 'Class B'), ('CC', 'Class C')], default='BD')),
            ],
        ),
    ]
