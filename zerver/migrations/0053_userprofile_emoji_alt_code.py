# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0052_auto_fix_realmalias_realm_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emoji_alt_code',
            field=models.BooleanField(default=False),
        ),
    ]
