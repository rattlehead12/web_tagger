# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-23 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_remove_tag_clasificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='oracion',
            name='clasificacion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='documentos.Clasificacion'),
            preserve_default=False,
        ),
    ]
