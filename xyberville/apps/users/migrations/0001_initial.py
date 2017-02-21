# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import xyberville.apps.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, unique=True, max_length=255, blank=True)),
                ('email', models.EmailField(max_length=255, null=True, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date joined')),
                ('type', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Ketua RW'), (2, b'Wakil Ketua RW'), (3, b'Sekretaris'), (4, b'Bendahara'), (5, b'Ketua RT')])),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('permissions', models.ManyToManyField(related_name='permissions', to='permissions.Permission')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', xyberville.apps.users.models.CustomUserManager()),
            ],
        ),
    ]
