# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170217_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='penyandang_cacat',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Tidak'), (2, b'Cacat Fisik'), (3, b'Tunanetra'), (4, b'Tunarungu'), (5, b'Cacat Mental'), (6, b'Cacat Fisik dan Mental'), (7, b'Lainnya')]),
        ),
    ]
