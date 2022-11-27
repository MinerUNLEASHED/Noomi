# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2022-11-23 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sets', '0002_auto_20221123_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='sets',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sets',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
