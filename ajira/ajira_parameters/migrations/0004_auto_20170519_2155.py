# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0003_auto_20170519_2132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Countries',
        ),
    ]
