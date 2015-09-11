# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20150904_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='uod_cadets',
            field=models.CharField(choices=[('PT', 'PT'), ('BDU', 'BDU'), ('Class A', 'Class A'), ('Class B', 'Class B'), ('Class C', 'Class C')], max_length=7, default='BDU'),
        ),
        migrations.AlterField(
            model_name='event',
            name='uod_senior',
            field=models.CharField(choices=[('PT', 'PT'), ('BDU', 'BDU'), ('Class A', 'Class A'), ('Class B', 'Class B'), ('Class C', 'Class C')], max_length=7, default='BDU'),
        ),
        migrations.AlterField(
            model_name='event',
            name='uod_staff',
            field=models.CharField(choices=[('PT', 'PT'), ('BDU', 'BDU'), ('Class A', 'Class A'), ('Class B', 'Class B'), ('Class C', 'Class C')], max_length=7, default='BDU'),
        ),
    ]
