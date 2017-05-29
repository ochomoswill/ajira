# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0005_auto_20170523_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='slug',
            field=models.SlugField(default='slug/%Y-%m-%d %H:%M:%S', max_length=250),
        ),
        migrations.AddField(
            model_name='worker',
            name='worker_avatar',
            field=models.ImageField(upload_to='ajiriwa_upload/%Y/%m/%d/', default='ajiriwa_upload/%Y/%m/%d/'),
        ),
    ]
