# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-21 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]