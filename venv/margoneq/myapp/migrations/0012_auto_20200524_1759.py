# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-24 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20200511_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='verifCode',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='verifyCodes',
        ),
    ]
