# Generated by Django 3.1.7 on 2021-04-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210407_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='axis',
            name='name',
            field=models.CharField(default='Axis Info', max_length=50),
        ),
    ]