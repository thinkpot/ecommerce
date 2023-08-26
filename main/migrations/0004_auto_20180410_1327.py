# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-10 13:27
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180410_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='favicon',
            field=mezzanine.core.fields.FileField(blank=True, help_text='A 16x16 px image that appears in the browser tab', max_length=255, verbose_name='Favicon'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='logo_small',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, verbose_name='Small Logo'),
        ),
    ]