# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(related_name='bought', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sale',
            name='sales_person',
            field=models.ForeignKey(related_name='sales', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(related_name='items', to='products.Product'),
        ),
        migrations.AddField(
            model_name='item',
            name='sale',
            field=models.ForeignKey(related_name='items', to='sales.Sale'),
        ),
    ]
