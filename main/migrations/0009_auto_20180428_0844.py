# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-28 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('main', '0008_auto_20180428_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iconblurb',
            name='homepage',
        ),
        migrations.AddField(
            model_name='iconblurb',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blurbs', to='pages.Page'),
            preserve_default=False,
        ),
    ]
