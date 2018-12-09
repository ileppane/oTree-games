# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-08 17:22
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('neutralvendor', '0002_auto_20181208_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='check2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='check3',
        ),
        migrations.AddField(
            model_name='player',
            name='check2high',
            field=otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '0'], [2, '1/7'], [3, '5/7']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='check2low',
            field=otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '0'], [2, '1/7'], [3, '5/7']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='check3high',
            field=otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='check3low',
            field=otree.db.models.PositiveIntegerField(blank=True, choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], null=True),
        ),
    ]
