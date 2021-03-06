# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('skillSet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSkills',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('skill', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='skillSet.skillSet')),
            ],
        ),
    ]
