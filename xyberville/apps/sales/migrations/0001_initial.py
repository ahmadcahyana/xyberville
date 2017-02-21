# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('price', models.FloatField(null=True, blank=True)),
                ('tax_amount', models.FloatField(null=True, blank=True)),
                ('product', models.ForeignKey(related_name='items', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=8, db_index=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, b'Pending'), (2, b'Paid'), (3, b'Completed'), (4, b'Canceled'), (5, b'Refunded')])),
                ('notes', models.TextField(blank=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('price', models.FloatField(null=True, blank=True)),
                ('discount', models.FloatField(null=True, blank=True)),
                ('amount_to_collect', models.FloatField(null=True, blank=True)),
                ('paid', models.DateTimeField(null=True, blank=True)),
                ('completed', models.DateTimeField(null=True, blank=True)),
                ('canceled', models.DateTimeField(null=True, blank=True)),
                ('cancellation_note', models.TextField(blank=True)),
                ('refunded', models.DateTimeField(null=True, blank=True)),
                ('refund_notes', models.TextField(blank=True)),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'1 - Bad'), (2, b'2'), (3, b'3 - Average'), (4, b'4'), (5, b'5 - Best')])),
                ('customer', models.ForeignKey(related_name='bought', to=settings.AUTH_USER_MODEL)),
                ('sales_person', models.ForeignKey(related_name='sales', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sale',
            field=models.ForeignKey(related_name='items', to='sales.Sale'),
        ),
    ]
