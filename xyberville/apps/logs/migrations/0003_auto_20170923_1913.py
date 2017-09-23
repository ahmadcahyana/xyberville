# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keluarga', '0002_auto_20170923_1913'),
        ('logs', '0002_userprofilelogs_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilelogs',
            name='user',
            field=models.ForeignKey(related_name='profile_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userlogs',
            name='user',
            field=models.ForeignKey(related_name='user_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userlogs',
            name='user_edited',
            field=models.ForeignKey(related_name='user_edited_logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='keluargalogs',
            name='keluarga',
            field=models.ForeignKey(related_name='keluarga_logs', to='keluarga.Keluarga'),
        ),
        migrations.AddField(
            model_name='keluargalogs',
            name='user',
            field=models.ForeignKey(related_name='keluarga_logs', to=settings.AUTH_USER_MODEL),
        ),
    ]
