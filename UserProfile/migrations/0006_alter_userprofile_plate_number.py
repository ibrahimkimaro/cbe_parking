# Generated by Django 5.0.4 on 2024-04-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0005_alter_userprofile_plate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='plate_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
