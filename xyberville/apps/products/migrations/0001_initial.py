# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=255, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price_per_unit', models.FloatField()),
                ('basic_unit', models.PositiveSmallIntegerField(choices=[(1, b'Kilograms'), (2, b'Litre'), (3, b'Centimetre'), (4, b'Pieces'), (5, b'Pax'), (6, b'Box')])),
                ('tax_percentage', models.FloatField()),
                ('limited', models.BooleanField(default=False)),
                ('active_for_sale', models.BooleanField(default=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('in_stock', models.FloatField()),
                ('product', models.OneToOneField(to='products.Product')),
            ],
        ),
    ]
