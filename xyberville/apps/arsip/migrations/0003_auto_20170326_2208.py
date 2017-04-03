# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0002_pengantar_warga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengantar',
            name='keperluan',
            field=models.PositiveSmallIntegerField(verbose_name=((1, b'Pembuatan KTP'), (2, b'Perbaikan Data KTP'), (3, b'Pembuatan SKCK'), (4, b'Domisili'), (5, b'Keterangan Pindah'), (6, b'Menikah'), (7, b'Cerai'), (8, b'Lainnya'))),
        ),
    ]
