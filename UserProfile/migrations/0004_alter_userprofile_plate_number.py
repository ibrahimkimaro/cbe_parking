# Generated by Django 5.0.4 on 2024-04-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_userprofile_plate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='plate_number',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
