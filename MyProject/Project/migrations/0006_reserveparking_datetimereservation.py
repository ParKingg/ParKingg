# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-23 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_checkoutticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserveparking',
            name='DateTimeReservation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
