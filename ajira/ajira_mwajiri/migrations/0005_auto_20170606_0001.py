# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0004_auto_20170601_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='employer_avatar',
            field=models.ImageField(default='mwajiri_upload/2017/06/01/logo_sd3RGNe.png', upload_to='mwajiri_upload/%Y/%m/%d/'),
        ),
    ]
