# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_customitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='customitem',
            name='itemname',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
