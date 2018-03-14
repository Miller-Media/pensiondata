# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-14 09:02
from __future__ import unicode_literals

from django.db import migrations
import pensiondata.models


class Migration(migrations.Migration):

    dependencies = [
        ('pensiondata', '0037_auto_20180314_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='census_plan_id',
            field=pensiondata.models.CharNullField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
