# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RukunTetanga',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rt', models.CharField(max_length=10)),
                ('alamat_sekretariat', models.CharField(max_length=255)),
                ('kode_pos', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='kop_surat')),
                ('start_periods', models.DateField()),
                ('end_periods', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RukunWarga',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rw', models.CharField(max_length=10)),
                ('alamat_sekretariat', models.CharField(max_length=255)),
                ('kode_pos', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='kop_surat')),
                ('start_periods', models.DateField()),
                ('end_periods', models.DateField()),
            ],
        ),
    ]
