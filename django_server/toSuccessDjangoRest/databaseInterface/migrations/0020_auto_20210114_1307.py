# Generated by Django 3.0.8 on 2021-01-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseInterface', '0019_auto_20210114_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='attrs',
            new_name='data',
        ),
        migrations.AlterField(
            model_name='activity',
            name='unique_id',
            field=models.IntegerField(default=682551),
        ),
    ]
