# Generated by Django 3.0.8 on 2020-07-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseInterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.CharField(max_length=250),
        ),
    ]
