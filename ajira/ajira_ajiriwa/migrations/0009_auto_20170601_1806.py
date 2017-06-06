# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0008_auto_20170524_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='experience',
            name='job_location',
            field=models.TextField(blank=True),
        ),
    ]
