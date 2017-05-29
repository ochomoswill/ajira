# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0004_auto_20170523_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='expected_salary',
            field=models.DecimalField(blank=True, max_digits=10, null=True, default='10000', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='preferred_locations',
            field=models.CharField(blank=True, max_length=100, null=True, default='Kitengela'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_bio',
            field=models.TextField(blank=True, null=True, default='I am ...'),
        ),
    ]
