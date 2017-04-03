# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('keluarga', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keluarga',
            name='kepala_keluarga',
            field=models.ForeignKey(related_name='family', verbose_name=b'Kepala Keluarga', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='keluarga',
            name='province',
            field=models.ForeignKey(to='regions.Province'),
        ),
        migrations.AddField(
            model_name='keluarga',
            name='regency',
            field=models.ForeignKey(to='regions.Regency'),
        ),
        migrations.AddField(
            model_name='keluarga',
            name='village',
            field=models.ForeignKey(to='regions.Village'),
        ),
    ]
