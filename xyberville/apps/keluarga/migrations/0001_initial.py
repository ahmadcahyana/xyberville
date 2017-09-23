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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nomor_kk', models.CharField(unique=True, verbose_name='Nomor KK', max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('rt', models.CharField(blank=True, max_length=255)),
                ('rw', models.CharField(blank=True, max_length=255)),
                ('telepon', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('district', models.ForeignKey(to='regions.District')),
            ],
            options={
                'verbose_name_plural': 'keluargas',
                'verbose_name': 'keluarga',
                'db_table': 'keluarga',
            },
        ),
    ]
