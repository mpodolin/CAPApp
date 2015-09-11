# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.contrib.auth.models
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True)),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('cap_id', models.IntegerField(default=0)),
                ('current_rank', models.IntegerField(default=0)),
                ('date_of_rank', models.DateField(blank=True, default=datetime.datetime.now)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime.now)),
                ('squadron', models.CharField(default='MD-011', max_length=6)),
                ('gender', models.CharField(default='M', max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('leadership_test', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('drill_test', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('aerospace_test', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('character_development', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('fitness_test', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('sda', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('speech', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('essay', models.CharField(default='I', max_length=1, choices=[('I', 'Incomplete'), ('C', 'Complete'), ('N', 'Not Required')])),
                ('groups', models.ManyToManyField(blank=True, related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_set', help_text='Specific permissions for this user.', related_query_name='user', verbose_name='user permissions', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
