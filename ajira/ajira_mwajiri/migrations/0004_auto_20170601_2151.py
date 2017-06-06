# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0003_auto_20170601_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='email_address',
            field=models.CharField(max_length=50, default='123@hotmail.com'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='employer_avatar',
            field=models.ImageField(upload_to='mwajiri_upload/%Y/%m/%d/', default='mwajiri_upload/2017/06/1/logo.png'),
        ),
    ]
