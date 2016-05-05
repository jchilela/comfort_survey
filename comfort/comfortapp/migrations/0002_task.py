# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comfortapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_name', models.CharField(max_length=100)),
                ('task_desc', models.CharField(max_length=100)),
            ],
        ),
    ]
