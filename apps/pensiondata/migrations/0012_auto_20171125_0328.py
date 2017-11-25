# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pensiondata', '0011_auto_20171125_0310'),
    ]

    operations = [

        migrations.AlterModelOptions(
            name='datasource',
            options={'managed': True, 'verbose_name': 'Data Source', 'verbose_name_plural': 'Data Sources'},
        ),

        migrations.AddField(
            model_name='plan',
            name='admin_gov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.Government'),
        ),
        migrations.AddField(
            model_name='plan',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),

        migrations.AddField(
            model_name='planannualattribute',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.Plan'),
        ),
        migrations.AddField(
            model_name='planannualattribute',
            name='plan_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='annual_attrs', to='pensiondata.PlanAttribute'),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='attribute_column_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.DataSource'),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='display_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='multiplier',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='planattribute',
            name='plan_attribute_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.PlanAttributeCategory'),
        ),

        migrations.RemoveField(
            model_name='planattribute',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='planattribute',
            name='category',
        ),

    ]
