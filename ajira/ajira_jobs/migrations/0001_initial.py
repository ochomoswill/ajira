# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('approval_status', models.CharField(choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('declined', 'DECLINED')], default='pending', max_length=20)),
                ('job_status', models.CharField(choices=[('vacant', 'VACANT'), ('filled', 'FILLED')], default='vacant', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employer_id', models.ForeignKey(to='ajira_mwajiri.Employer')),
            ],
        ),
    ]
