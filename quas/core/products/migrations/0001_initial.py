# Generated by Django 3.1.7 on 2021-07-19 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('calculators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
                ('year_of_foundation', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
                ('main_slug', models.CharField(max_length=200)),
                ('product_type', models.CharField(choices=[('IR', 'Industrial Robots'), ('RGV', 'RGV Robots'), ('CO', 'Cobots'), ('WM', 'Welding Machines')], max_length=10)),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger'), ('A', 'success'), ('W', 'warning')], max_length=1)),
                ('slogan', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
                ('image', models.ImageField(upload_to='robots/images')),
                ('type', models.CharField(choices=[('default', 'Default'), ('working_range', 'Working Range')], max_length=250)),
                ('is_active', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_direct_proportion', models.BooleanField()),
                ('coefficient_mapping', models.JSONField(blank=True, default=dict, null=True)),
                ('product_type', models.CharField(blank=True, choices=[('IR', 'Industrial Robots'), ('RGV', 'RGV Robots'), ('CO', 'Cobots'), ('WM', 'Welding Machines')], max_length=250, null=True)),
                ('data_type', models.CharField(choices=[('int', 'Integer'), ('dec', 'Decimal'), ('str', 'String'), ('list', 'List'), ('dict', 'Dict')], max_length=50)),
                ('attribute_groups', models.ManyToManyField(to='products.AttributeGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=350, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('extra_fields', models.JSONField(blank=True, default=dict, null=True)),
                ('value', models.JSONField(default=dict)),
                ('conf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attributeconf')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('value_calculator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculators.valuecalculator')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
