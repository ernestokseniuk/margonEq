# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-27 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20200527_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlvl',
            name='color',
            field=models.CharField(default=0, max_length=7),
            preserve_default=False,
        ),
    ]
