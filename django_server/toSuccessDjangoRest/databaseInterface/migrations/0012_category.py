# Generated by Django 3.0.8 on 2021-01-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseInterface', '0011_auto_20201228_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=15)),
                ('user', models.CharField(max_length=250)),
            ],
        ),
    ]