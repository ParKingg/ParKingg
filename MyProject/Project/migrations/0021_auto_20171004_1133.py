# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 03:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0020_auto_20171003_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationfee',
            name='Plate_no',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationfee',
            name='Slot_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationfee',
            name='Time_in',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkoutticket',
            name='DateTime_out',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 32, 34, 893259)),
        ),
        migrations.AlterField(
            model_name='reservationfee',
            name='DateTime_paid',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 32, 34, 893259)),
        ),
        migrations.AlterField(
            model_name='reserveparking',
            name='DateTimeReservation',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 4, 11, 32, 34, 893259)),
        ),
    ]
