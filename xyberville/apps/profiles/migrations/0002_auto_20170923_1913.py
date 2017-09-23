# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pekerjaan', '0001_initial'),
        ('keluarga', '0002_auto_20170923_1913'),
        ('regions', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ayah',
            field=models.ForeignKey(blank=True, related_name='ayah', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.ForeignKey(to='regions.District'),
        ),
        migrations.AddField(
            model_name='profile',
            name='ibu',
            field=models.ForeignKey(blank=True, related_name='ibu', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='keluarga',
            field=models.ForeignKey(blank=True, related_name='keluarga', null=True, to='keluarga.Keluarga'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pekerjaan',
            field=models.ForeignKey(blank=True, related_name='pekerjaan', null=True, to='pekerjaan.Pekerjaan'),
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
            field=models.ForeignKey(blank=True, related_name='tempat_lahir', null=True, to='regions.Regency'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='village',
            field=models.ForeignKey(to='regions.Village'),
        ),
    ]
