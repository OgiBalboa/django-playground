# Generated by Django 3.1.4 on 2021-01-09 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_robot_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
