# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-18 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientAPI', '0003_auto_20181018_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencytrendinginfo',
            name='lasttradeid',
            field=models.CharField(blank=True, default=1, max_length=30),
            preserve_default=False,
        ),
    ]
