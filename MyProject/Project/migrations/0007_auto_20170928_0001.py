# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0006_reserveparking_datetimereservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationFee',
            fields=[
                ('Receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_Fname', models.CharField(max_length=255)),
                ('Customer_Lname', models.CharField(max_length=255)),
                ('Item_Cost', models.PositiveIntegerField()),
                ('Item_Name', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
                ('DateTime_paid', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='Profile_Pic',
            field=models.ImageField(blank=True, upload_to='display_pictures'),
        ),
        migrations.AddField(
            model_name='checkoutticket',
            name='Plateno',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkoutticket',
            name='Slotno',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationfee',
            name='User_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.Account'),
        ),
    ]
