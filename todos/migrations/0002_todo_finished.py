# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
