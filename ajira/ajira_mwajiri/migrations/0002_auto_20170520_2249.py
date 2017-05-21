# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='email_address',
            field=models.CharField(max_length=50, default='123@example.com'),
        ),
        migrations.AddField(
            model_name='employer',
            name='user_password',
            field=models.CharField(max_length=50, default='1234'),
        ),
    ]
