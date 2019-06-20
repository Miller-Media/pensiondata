# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-30 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pensiondata', '0044_auto_20180316_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='PensionChartData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('f1_header', models.CharField(max_length=255)),
                ('f1_value', models.DecimalField(decimal_places=0, max_digits=12)),
                ('f2_header', models.CharField(blank=True, max_length=255)),
                ('f2_value', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PensionMapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('government_id', models.IntegerField()),
                ('government_name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=4)),
                ('plan_contributions', models.DecimalField(decimal_places=0, max_digits=12)),
                ('plan_liabilities', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanAnnualMasterAttribute',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=4)),
                ('attribute_value', models.CharField(blank=True, max_length=256, null=True)),
                ('is_from_source', models.NullBooleanField(default=None, help_text='check if the value is from source or from user just for Master Attribute')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.Plan')),
                ('plan_attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='annual_master_attrs', to='pensiondata.PlanAttribute')),
            ],
            options={
                'verbose_name': 'Plan Annual Master Attribute',
                'verbose_name_plural': 'Import Plan Annual Master Attributes',
                'db_table': 'plan_annual_master_attribute',
            },
        ),
        migrations.CreateModel(
            name='PlanAttributeMaster',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField()),
                ('data_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.DataSource')),
            ],
            options={
                'verbose_name': 'Plan Attribute Master',
                'db_table': 'plan_attribute_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlanMasterAttributeNames',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Plan Master Attribute Name',
                'verbose_name_plural': 'Plan Master Attribute Names',
                'db_table': 'plan_master_attribute_names',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='planattributemaster',
            name='master_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.PlanMasterAttributeNames'),
        ),
        migrations.AddField(
            model_name='planattributemaster',
            name='plan_attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pensiondata.PlanAttribute'),
        ),
        migrations.AlterUniqueTogether(
            name='planannualmasterattribute',
            unique_together=set([('plan', 'year', 'plan_attribute')]),
        ),
    ]