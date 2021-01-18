# Generated by Django 3.1.4 on 2021-01-09 19:01

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_robot_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='axis1_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis1_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis2_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis2_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis3_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis3_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis4_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis4_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis5_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis5_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis6_movement',
            field=models.CharField(blank=True, choices=[('R', 'Rotation'), ('A', 'Arm'), ('W', 'Wrist'), ('B', 'Bend'), ('T', 'Turn')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='axis6_speed',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='customer_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='mounting',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('A', 'Any'), ('F', 'Floor'), ('W', 'Wall'), ('T', 'Tilted'), ('I', 'Invert Mount')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='number_of_axes',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='robot',
            name='overall_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='payload',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='picking_cycle',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='reach',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='repeatability',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='slogan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='robot',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='robot',
            name='working_range_image',
            field=models.ImageField(blank=True, null=True, upload_to='robots/working_range_images/'),
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brand')),
            ],
        ),
        migrations.AddField(
            model_name='robot',
            name='controller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.controller'),
        ),
    ]