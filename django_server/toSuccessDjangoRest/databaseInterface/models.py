from django.db import models
import random

# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length=250)
    activity_category = models.CharField(max_length=250, default="undefined")
    minutes_after_midnight_start = models.IntegerField()
    minutes_after_midnight_end = models.IntegerField()
    date = models.IntegerField()
    date_string = models.CharField(max_length=50, default="0-Jan-0000")
    user = models.CharField(max_length=250, default='user')
    unique_id = models.IntegerField(default=random.randint(0, 1000000))

    class meta:
        ordering = ['created']

class Category(models.Model):
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=15)
    user = models.CharField(max_length=250)
    unique_id = models.IntegerField(default=0)

    class meta:
        ordering = ['created']

# For stats page
class CategoryStats(models.Model):
    name = models.CharField(max_length=50)

    class meta:
        ordering = ['created']

class KeyVal(models.Model):
    container = models.ForeignKey(CategoryStats, db_index=True, on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=240, db_index=True)
    time_value = models.CharField(max_length=240, db_index=True)
