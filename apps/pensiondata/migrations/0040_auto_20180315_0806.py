# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-15 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pensiondata', '0039_auto_20180315_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='government',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='government',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=12, null=True),
        ),
    ]