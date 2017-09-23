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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'districts',
                'verbose_name': 'district',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'provinces',
                'verbose_name': 'province',
            },
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(unique=True, max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('province', models.ForeignKey(db_column='province_code', to='regions.Province', to_field='code')),
            ],
            options={
                'verbose_name_plural': 'regencies',
                'verbose_name': 'regency',
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(db_column='district_code', to='regions.District', to_field='code')),
            ],
            options={
                'verbose_name_plural': 'villages',
                'verbose_name': 'village',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='regency',
            field=models.ForeignKey(db_column='regency_code', to='regions.Regency', to_field='code'),
        ),
    ]
