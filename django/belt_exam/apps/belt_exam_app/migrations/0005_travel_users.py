# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0004_travel'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='users',
            field=models.ManyToManyField(related_name='travels', to='belt_exam_app.User'),
        ),
    ]