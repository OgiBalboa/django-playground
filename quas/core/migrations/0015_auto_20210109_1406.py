# Generated by Django 3.1.4 on 2021-01-09 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20210109_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.brand'),
        ),
    ]
