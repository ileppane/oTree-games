# Generated by Django 2.2.4 on 2020-02-15 13:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('eoq', '0003_auto_20200215_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='totalholdingcost',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='totalordercost',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='orderquantity',
            field=otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, null=True),
        ),
    ]
