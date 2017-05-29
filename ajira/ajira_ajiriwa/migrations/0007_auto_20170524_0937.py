# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0006_auto_20170524_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='slug',
            field=models.SlugField(default='dog-poo', max_length=250),
        ),
    ]
