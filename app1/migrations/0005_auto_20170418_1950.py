# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_dueno_fecha_nac'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarifas',
            old_name='cantidad',
            new_name='precio',
        ),
    ]
