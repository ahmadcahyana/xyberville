# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regions', '0001_initial'),
        ('struktur_organisasi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rukunwarga',
            name='bendahara',
            field=models.ForeignKey(blank=True, related_name='bendahara_rw', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='district',
            field=models.ForeignKey(to='regions.District'),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='ketua',
            field=models.ForeignKey(blank=True, related_name='ketua_rw', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='province',
            field=models.ForeignKey(to='regions.Province'),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='regency',
            field=models.ForeignKey(to='regions.Regency'),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='sekretaris',
            field=models.ForeignKey(blank=True, related_name='sekretaris_rw', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='village',
            field=models.ForeignKey(to='regions.Village'),
        ),
        migrations.AddField(
            model_name='rukunwarga',
            name='wakil',
            field=models.ForeignKey(blank=True, related_name='wakil_rw', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='bendahara',
            field=models.ForeignKey(blank=True, related_name='bendahara_rt', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='district',
            field=models.ForeignKey(to='regions.District'),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='ketua',
            field=models.ForeignKey(blank=True, related_name='ketua_rt', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='province',
            field=models.ForeignKey(to='regions.Province'),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='regency',
            field=models.ForeignKey(to='regions.Regency'),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='sekretaris',
            field=models.ForeignKey(blank=True, related_name='sekretaris_rt', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='village',
            field=models.ForeignKey(to='regions.Village'),
        ),
        migrations.AddField(
            model_name='rukuntetanga',
            name='wakil',
            field=models.ForeignKey(blank=True, related_name='wakil_rt', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
