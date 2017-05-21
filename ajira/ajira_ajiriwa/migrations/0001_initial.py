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
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(default=django.utils.timezone.now)),
                ('approval_status', models.CharField(max_length=20, default='pending', choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('declined', 'DECLINED')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('worker_name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
                ('skills', models.TextField()),
                ('birth_year', models.DateField(default=django.utils.timezone.now)),
                ('mobile_no', models.IntegerField()),
                ('approval_status', models.CharField(max_length=20, default='pending', choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('declined', 'DECLINED')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('constituency_id', models.ForeignKey(to='ajira_parameters.Constituencies')),
                ('country_id', models.ForeignKey(to='ajira_parameters.Countries')),
                ('county_id', models.ForeignKey(to='ajira_parameters.Counties')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='worker_id',
            field=models.ForeignKey(to='ajira_ajiriwa.Worker'),
        ),
    ]
