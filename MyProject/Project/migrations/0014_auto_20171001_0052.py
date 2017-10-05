# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 16:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_auto_20171001_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionhistory',
            name='Payment_Status',
        ),
        migrations.AlterField(
            model_name='checkoutticket',
            name='DateTime_out',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 0, 52, 34, 606648)),
        ),
        migrations.AlterField(
            model_name='reservationfee',
            name='DateTime_paid',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 0, 52, 34, 607649)),
        ),
        migrations.AlterField(
            model_name='reserveparking',
            name='DateTimeReservation',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 0, 52, 34, 606115)),
        ),
    ]