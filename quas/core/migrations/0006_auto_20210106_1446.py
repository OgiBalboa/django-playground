# Generated by Django 3.1.4 on 2021-01-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210106_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('IR', 'Endustriyel Robotlar'), ('RGV', 'RGV Robotlar'), ('CO', 'Cobotlar')], max_length=4),
        ),
    ]