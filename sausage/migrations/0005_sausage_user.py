# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sausage', '0004_auto_20170412_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='sausage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
