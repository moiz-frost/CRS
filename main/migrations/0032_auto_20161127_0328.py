# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20161127_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
