# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'district',
                'verbose_name_plural': 'districts',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'provinces',
            },
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('province', models.ForeignKey(to='regions.Province', db_column=b'province_code', to_field=b'code')),
            ],
            options={
                'verbose_name': 'regency',
                'verbose_name_plural': 'regencies',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(to='regions.District', db_column=b'district_code', to_field=b'code')),
            ],
            options={
                'verbose_name': 'village',
                'verbose_name_plural': 'villages',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='regency',
            field=models.ForeignKey(to='regions.Regency', db_column=b'regency_code', to_field=b'code'),
        ),
    ]
