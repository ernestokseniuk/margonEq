# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_customitem_kontra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customitem',
            name='SA',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='absFiz',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='absMag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='atakBlysk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='atakFizMax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='atakOg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='atakZim',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='atakfizmin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='autor',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='blok',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='blokprze',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='ck',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='energia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='fizycznyck',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='grprc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='grsil',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='kontra',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='lvl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='magicznyck',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='mana',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='niszAbs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='niszEne',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='niszMan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='niszPan',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='niszczOdporn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='obnCk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='obnSA',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='obnUniku',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='odpBlysk',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='odpOg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='odpTrut',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='odpZim',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='panc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='przebicie',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='przywr',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='sil',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='spowalniaCel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='trucizna',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='unik',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='wszystkieCechy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customitem',
            name='zren',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
