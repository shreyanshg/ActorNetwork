# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
