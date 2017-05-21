# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='email_address',
            field=models.CharField(default='123@example.com', max_length=50),
        ),
        migrations.AddField(
            model_name='worker',
            name='user_password',
            field=models.CharField(default='1234', max_length=50),
        ),
    ]
