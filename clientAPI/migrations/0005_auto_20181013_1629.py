# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-13 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientAPI', '0004_auto_20181013_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency_trending_info',
            name='changepct24hour',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
