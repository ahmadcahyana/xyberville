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
            name='KeluargaLogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.PositiveIntegerField(choices=[(1, b'Created'), (2, b'Edited')])),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.PositiveIntegerField(choices=[(1, b'Created'), (2, b'Edited')])),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileLogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.PositiveIntegerField(choices=[(1, b'Created'), (2, b'Edited')])),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
