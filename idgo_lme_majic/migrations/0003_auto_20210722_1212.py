# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-22 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idgo_lme_majic', '0002_auto_20210722_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermajiclme',
            name='date_expiration_lme',
            field=models.DateField(blank=True, null=True, verbose_name="Date d'expiration LME"),
        ),
        migrations.AlterField(
            model_name='usermajiclme',
            name='date_expiration_majic',
            field=models.DateField(blank=True, null=True, verbose_name="Date d'expiration MAJIC"),
        ),
    ]
