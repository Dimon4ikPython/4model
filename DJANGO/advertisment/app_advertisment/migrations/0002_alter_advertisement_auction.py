# Generated by Django 4.2.3 on 2023-08-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE app_advertisment_advertisement RENAME TO advertisement;'),
    ]