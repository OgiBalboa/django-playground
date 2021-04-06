# Generated by Django 3.1.7 on 2021-04-06 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210406_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='axis',
            name='robot',
        ),
        migrations.AddField(
            model_name='robot',
            name='axis',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.axis'),
        ),
    ]