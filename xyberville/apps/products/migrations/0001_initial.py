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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product_code', models.CharField(max_length=255, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price_per_unit', models.FloatField()),
                ('basic_unit', models.PositiveSmallIntegerField(choices=[(1, 'Kilograms'), (2, 'Litre'), (3, 'Centimetre'), (4, 'Pieces'), (5, 'Pax'), (6, 'Box')])),
                ('tax_percentage', models.FloatField()),
                ('limited', models.BooleanField(default=False)),
                ('active_for_sale', models.BooleanField(default=True)),
                ('discounted_price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('in_stock', models.FloatField()),
                ('product', models.OneToOneField(to='products.Product')),
            ],
        ),
    ]
