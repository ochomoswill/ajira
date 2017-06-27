# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_ajiriwa', '0009_auto_20170601_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=50)),
                ('message_status', models.CharField(choices=[('read', 'READ'), ('unread', 'UNREAD')], max_length=50, default='UNREAD')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
                ('worker_id', models.ForeignKey(to='ajira_ajiriwa.Worker')),
            ],
        ),
    ]
