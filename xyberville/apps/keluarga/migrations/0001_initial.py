# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keluarga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomor_kk', models.CharField(unique=True, max_length=255, verbose_name=b'Nomor KK')),
                ('alamat', models.CharField(max_length=255)),
                ('rt', models.CharField(max_length=255)),
                ('rw', models.CharField(max_length=255)),
                ('telepon', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('district', models.ForeignKey(to='regions.District')),
            ],
            options={
                'db_table': 'keluarga',
                'verbose_name': 'keluarga',
                'verbose_name_plural': 'keluargas',
            },
        ),
    ]
