# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0001_initial'),
        ('ajira_ajiriwa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('relationship', models.TextField()),
                ('position_or_skills_at_that_time', models.TextField()),
                ('remark', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employer_id', models.ForeignKey(to='ajira_mwajiri.Employer')),
                ('worker_id', models.ForeignKey(to='ajira_ajiriwa.Worker')),
            ],
        ),
    ]
