# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-30 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_auto_20200529_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
