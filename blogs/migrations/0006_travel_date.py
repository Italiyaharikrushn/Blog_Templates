# Generated by Django 5.1.3 on 2024-11-23 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_travel_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
