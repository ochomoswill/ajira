# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0005_counties'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constituencies',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('constituency_name', models.CharField(max_length=50)),
                ('county_id', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
