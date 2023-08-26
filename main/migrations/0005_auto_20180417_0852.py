# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-17 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('main', '0004_auto_20180410_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', mezzanine.core.fields.FileField(blank=True, max_length=255, verbose_name='Logo')),
                ('logo_small', mezzanine.core.fields.FileField(blank=True, max_length=255, verbose_name='Small Logo')),
                ('favicon', mezzanine.core.fields.FileField(blank=True, help_text='An image that appears in the browser tab', max_length=255, verbose_name='Favicon')),
                ('site', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Site Configuration',
                'verbose_name_plural': 'Site Configuration',
            },
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='favicon',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='logo_small',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='footer_subscribe_info',
            field=models.CharField(default='Pellentesque habitant morbi tristique senectus et netus \t\t\t\tet malesuada fames ac turpis egestas.', help_text='Text displayed above the subscription email field.', max_length=200),
        ),
    ]
