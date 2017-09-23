# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import xyberville.apps.users.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(blank=True, unique=True, max_length=255, db_index=True)),
                ('email', models.EmailField(blank=True, null=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('type', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Ketua RW'), (2, 'Wakil Ketua RW'), (3, 'Sekretaris'), (4, 'Bendahara'), (5, 'Ketua RT')])),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', related_query_name='user', related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('permissions', models.ManyToManyField(related_name='permissions', to='permissions.Permission')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', related_query_name='user', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', xyberville.apps.users.models.CustomUserManager()),
            ],
        ),
    ]
