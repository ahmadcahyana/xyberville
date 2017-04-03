# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pekerjaan', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
        ('keluarga', '0002_auto_20170326_2204'),
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ayah',
            field=models.ForeignKey(related_name='ayah', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.ForeignKey(to='regions.District'),
        ),
        migrations.AddField(
            model_name='profile',
            name='ibu',
            field=models.ForeignKey(related_name='ibu', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='keluarga',
            field=models.ForeignKey(related_name='keluarga', blank=True, to='keluarga.Keluarga', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pekerjaan',
            field=models.ForeignKey(related_name='pekerjaan', blank=True, to='pekerjaan.Pekerjaan', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='province',
            field=models.ForeignKey(to='regions.Province'),
        ),
        migrations.AddField(
            model_name='profile',
            name='regency',
            field=models.ForeignKey(to='regions.Regency'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tempat_lahir',
            field=models.ForeignKey(related_name='tempat_lahir', blank=True, to='regions.Regency', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='village',
            field=models.ForeignKey(to='regions.Village'),
        ),
    ]
