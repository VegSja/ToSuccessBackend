from django.db import models

# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length=250)
    minutes_after_midnight_start = models.IntegerField()
    minutes_after_midnight_end = models.IntegerField()
    date = models.IntegerField()
    date_string = models.CharField(max_length=50, default="0-Jan-0000")
    user = models.CharField(max_length=250, default='user')

    class meta:
        ordering = ['created']
