# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0002_auto_20170520_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='expected_salary',
            field=models.DecimalField(decimal_places=2, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='worker',
            name='preferred_locations',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='worker_bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='email_address',
            field=models.EmailField(max_length=254, default='123@example.com'),
        ),
    ]
