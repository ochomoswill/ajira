# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0006_constituencies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituencies',
            name='county_id',
            field=models.ForeignKey(to='ajira_parameters.Counties'),
        ),
    ]
