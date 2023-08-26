# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-06 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('product_heading', models.CharField(default='Hot This Week', help_text='A header displayed above the products.', max_length=100)),
                ('second_slider_heading', models.CharField(default='GET INSPIRED', help_text='A header displayed above the 2nd slider.', max_length=100)),
                ('second_slider_subheading', models.CharField(default='Get the inspiration from our world class designers', help_text='A subheader displayed above the 2nd slider.', max_length=100)),
                ('blog_heading', models.CharField(default='FROM OUR BLOG', help_text='A header displayed above blog entries', max_length=100)),
                ('blog_subheading', models.CharField(default="What's new in the world of fashion? Check our blog!", help_text='A subheader displayed above blog entries', max_length=100)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='IconBlurb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('icon_class', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.CharField(blank=True, help_text='Optional, if provided clicking the blurb will go here.', max_length=2000)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blurbs', to='main.Homepage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
