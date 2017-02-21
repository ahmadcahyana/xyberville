# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keluarga', '0003_remove_keluarga_kepala_keluarga'),
    ]

    operations = [
        migrations.AddField(
            model_name='keluarga',
            name='kepala_keluarga',
            field=models.ForeignKey(related_name='family', verbose_name=b'Kepala Keluarga', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
