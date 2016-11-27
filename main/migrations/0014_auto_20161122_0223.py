# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20161122_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Person'),
        ),
    ]
