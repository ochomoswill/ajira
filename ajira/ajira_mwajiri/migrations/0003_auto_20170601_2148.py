# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_mwajiri', '0002_auto_20170520_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='employer_avatar',
            field=models.ImageField(upload_to='mwajiri_upload/%Y/%m/%d/', default='mwajiri_upload/2017/05/24/male.jpg'),
        ),
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.SlugField(max_length=250, default='dog-poo'),
        ),
    ]
