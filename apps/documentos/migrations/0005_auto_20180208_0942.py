# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-08 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_auto_20180208_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='texto',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
