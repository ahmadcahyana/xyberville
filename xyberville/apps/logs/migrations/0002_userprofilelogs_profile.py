# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilelogs',
            name='profile',
            field=models.ForeignKey(related_name='profile_logs', to='profiles.Profile'),
        ),
    ]
