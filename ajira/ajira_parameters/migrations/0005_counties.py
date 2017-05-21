# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0004_auto_20170519_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('county_code', models.IntegerField()),
                ('county_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('country_id', models.ForeignKey(to='ajira_parameters.Countries')),
            ],
        ),
    ]
