# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0007_auto_20170524_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='worker_avatar',
            field=models.ImageField(default='ajiriwa_upload/2017/05/24/male.jpg', upload_to='ajiriwa_upload/%Y/%m/%d/'),
        ),
    ]
