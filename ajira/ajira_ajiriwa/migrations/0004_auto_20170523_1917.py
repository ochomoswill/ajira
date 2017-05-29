# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0003_auto_20170523_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='expected_salary',
            field=models.DecimalField(default='10000', max_digits=10, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='preferred_locations',
            field=models.CharField(default='Kitengela', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_bio',
            field=models.TextField(default='I am ...', null=True),
        ),
    ]
