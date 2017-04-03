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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jenis', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pengantar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomor_surat', models.CharField(max_length=255)),
                ('keperluan', models.PositiveIntegerField(verbose_name=((1, b'Pembuatan KTP'), (2, b'Perbaikan Data KTP'), (3, b'Pembuatan SKCK'), (4, b'Domisili'), (5, b'Keterangan Pindah'), (6, b'Menikah'), (7, b'Cerai'), (8, b'Lainnya')))),
                ('lainnya', models.TextField(blank=True)),
                ('tanggal', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('jenis', models.ForeignKey(to='arsip.Klasifikasi')),
            ],
        ),
    ]
