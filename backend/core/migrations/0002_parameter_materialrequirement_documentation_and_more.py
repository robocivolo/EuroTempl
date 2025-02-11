# Generated by Django 4.2.18 on 2025-02-11 07:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.JSONField()),
                ('unit', models.CharField(blank=True, max_length=50)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.component')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MaterialRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_code', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=50)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.component')),
            ],
            options={
                'ordering': ['material_code'],
            },
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('document_type', models.CharField(max_length=50)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.component')),
            ],
            options={
                'verbose_name_plural': 'documentation',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ComponentInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.GeometryField(dim=3, srid=4326)),
                ('properties', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.component')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
