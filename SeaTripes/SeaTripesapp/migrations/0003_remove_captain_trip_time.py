# Generated by Django 4.1.3 on 2022-11-16 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SeaTripesapp', '0002_trip_captain_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='captain',
            name='trip_time',
        ),
    ]
