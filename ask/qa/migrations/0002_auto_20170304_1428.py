# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
