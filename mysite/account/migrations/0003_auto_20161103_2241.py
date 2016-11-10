# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161022_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='joined',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]