# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-19 11:56
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('datingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='appchoice',
            field=otree.db.models.StringField(choices=[('Dating App', 'Dating App'), ('Digital Marketing', 'Digital Marketing')], max_length=10000, null=True),
        ),
    ]