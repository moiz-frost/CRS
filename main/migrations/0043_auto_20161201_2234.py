# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 17:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20161201_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='crime_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crime',
            name='details',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='crimecategory',
            name='category_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crimecategory',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='crimecategory',
            name='penalty',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='crimecategory',
            name='threat_level',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='crimescommitted',
            name='crime',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Crime'),
        ),
        migrations.AlterField(
            model_name='crimescommitted',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='crimescommitted',
            name='suspect',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Suspect'),
        ),
        migrations.AlterField(
            model_name='crimescommitted',
            name='victim',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Victim'),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='age',
            field=models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator('^\\d{1,3}$', message='Invalid Age')]),
        ),
        migrations.AlterField(
            model_name='suspect',
            name='suspect_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='victim',
            name='age',
            field=models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator('^\\d{1,3}$', message='Invalid Age')]),
        ),
        migrations.AlterField(
            model_name='victim',
            name='cast',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='victim',
            name='complexion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='victim',
            name='gender',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='victim',
            name='profession',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='victim',
            name='victim_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
