# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0007_auto_20170520_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('employer_name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
                ('approval_status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('declined', 'DECLINED')], default='pending', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('constituency_id', models.ForeignKey(to='ajira_parameters.Constituencies')),
                ('country_id', models.ForeignKey(to='ajira_parameters.Countries')),
                ('county_id', models.ForeignKey(to='ajira_parameters.Counties')),
            ],
        ),
    ]
