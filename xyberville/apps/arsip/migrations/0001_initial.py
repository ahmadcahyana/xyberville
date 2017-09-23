# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klasifikasi',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('jenis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pengantar',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nomor_surat', models.CharField(max_length=255)),
                ('keperluan', models.PositiveSmallIntegerField(choices=[(1, 'Pembuatan KTP'), (2, 'Perbaikan Data KTP'), (3, 'Pembuatan SKCK'), (4, 'Domisili'), (5, 'Keterangan Pindah'), (6, 'Menikah'), (7, 'Cerai'), (8, 'Lainnya')])),
                ('lainnya', models.TextField(blank=True)),
                ('tanggal', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('jenis', models.ForeignKey(to='arsip.Klasifikasi')),
            ],
        ),
    ]
