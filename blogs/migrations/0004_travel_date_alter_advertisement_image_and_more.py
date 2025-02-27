# Generated by Django 5.1.3 on 2024-11-23 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_advertisement_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='biography',
            name='profile_img',
            field=models.ImageField(upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image_url',
            field=models.ImageField(upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='myself',
            name='video',
            field=models.FileField(upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='postpage',
            name='image_url',
            field=models.ImageField(upload_to='profile_images/'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='image_url',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]
