# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='seen_stauts',
            field=models.CharField(default='unseen', max_length=50),
        ),
    ]
