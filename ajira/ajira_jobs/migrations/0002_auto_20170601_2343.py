# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0007_auto_20170520_0004'),
        ('ajira_jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='constituency_id',
            field=models.ForeignKey(default=1, to='ajira_parameters.Constituencies'),
        ),
        migrations.AddField(
            model_name='job',
            name='county_id',
            field=models.ForeignKey(default=1, to='ajira_parameters.Counties'),
        ),
    ]
