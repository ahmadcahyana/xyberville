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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rt', models.CharField(max_length=10)),
                ('alamat_sekretariat', models.CharField(max_length=255)),
                ('kode_pos', models.CharField(max_length=255, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'kop_surat', blank=True)),
                ('start_periods', models.DateField()),
                ('end_periods', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RukunWarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rw', models.CharField(max_length=10)),
                ('alamat_sekretariat', models.CharField(max_length=255)),
                ('kode_pos', models.CharField(max_length=255, blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'kop_surat', blank=True)),
                ('start_periods', models.DateField()),
                ('end_periods', models.DateField()),
            ],
        ),
    ]
