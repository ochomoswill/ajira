# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0005_auto_20170606_0001'),
        ('ajira_ajiriwa', '0009_auto_20170601_1806'),
        ('ajira_jobs', '0003_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('worker_phone_no', models.IntegerField()),
                ('applicant_status', models.CharField(default='pending', max_length=20, choices=[('approved', 'APPROVED'), ('pending', 'PENDING'), ('declined', 'DECLINED')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('employer_id', models.ForeignKey(to='ajira_mwajiri.Employer')),
                ('job_id', models.ForeignKey(to='ajira_jobs.Job')),
                ('worker_id', models.ForeignKey(to='ajira_ajiriwa.Worker')),
            ],
        ),
    ]
