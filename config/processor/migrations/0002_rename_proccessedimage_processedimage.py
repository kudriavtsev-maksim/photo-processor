# Generated by Django 5.2 on 2025-04-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProccessedImage',
            new_name='ProcessedImage',
        ),
    ]
