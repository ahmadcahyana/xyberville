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
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('tax_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=8, db_index=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Paid'), (3, 'Completed'), (4, 'Canceled'), (5, 'Refunded')])),
                ('notes', models.TextField(blank=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('price', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('amount_to_collect', models.FloatField(blank=True, null=True)),
                ('paid', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('canceled', models.DateTimeField(blank=True, null=True)),
                ('cancellation_note', models.TextField(blank=True)),
                ('refunded', models.DateTimeField(blank=True, null=True)),
                ('refund_notes', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, '1 - Bad'), (2, '2'), (3, '3 - Average'), (4, '4'), (5, '5 - Best')])),
            ],
        ),
    ]
