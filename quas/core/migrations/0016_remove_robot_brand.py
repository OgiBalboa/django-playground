# Generated by Django 3.1.4 on 2021-01-09 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210109_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='brand',
        ),
    ]
