# Generated by Django 3.0.8 on 2021-01-15 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseInterface', '0022_auto_20210115_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='unique_id',
            field=models.IntegerField(default=43896),
        ),
    ]