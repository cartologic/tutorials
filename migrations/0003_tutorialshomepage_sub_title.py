# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-02 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20190402_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialshomepage',
            name='sub_title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
