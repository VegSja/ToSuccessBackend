# Generated by Django 3.0.8 on 2021-01-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseInterface', '0026_auto_20210115_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='unique_id',
            field=models.IntegerField(default=818949),
        ),
        migrations.AlterField(
            model_name='stats',
            name='username',
            field=models.CharField(default='not_defined', max_length=250),
        ),
    ]