# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-18 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZenVector', '0004_auto_20191109_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_deadline',
            field=models.DateField(),
        ),
    ]
