from datetime import date, datetime
from django.utils import timezone
from django.db import models


class Event(models.Model):
    # Event properties
    title = models.CharField(max_length=200, default='Weekly Meeting')
    location = models.CharField(max_length=200, blank=True)
    weekly_meeting = models.BooleanField(default=True)
    activities = models.TextField(blank=True)
    start = models.DateTimeField(default=timezone.now, blank=True)
    end = models.DateTimeField(default=timezone.now, blank=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    squadron = models.CharField(max_length=6, default='MD-011')

    # Uniform Options
    PT = 'PT'
    BDU = 'BDU'
    CLASS_A = 'Class A'
    CLASS_B = 'Class B'
    CLASS_C = 'Class C'
    UNIFORM_CHOICES = (
        (PT, 'PT'),
        (BDU, 'BDU'),
        (CLASS_A, 'Class A'),
        (CLASS_B, 'Class B'),
        (CLASS_C, 'Class C'),
    )
    uod_cadets = models.CharField(max_length=7, choices=UNIFORM_CHOICES, default=BDU)
    uod_staff = models.CharField(max_length=7, choices=UNIFORM_CHOICES, default=BDU)
    uod_senior = models.CharField(max_length=7, choices=UNIFORM_CHOICES, default=BDU)

    def start_month(self):
        return self.start.date


    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.title
