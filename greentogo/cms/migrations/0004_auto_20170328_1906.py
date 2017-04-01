# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20170326_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='repeat_in_subnav',
            field=models.BooleanField(
                default=False,
                help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.",
                verbose_name='repeat in sub-navigation'
            ),
        ),
        migrations.AddField(
            model_name='homepage',
            name='repeated_item_text',
            field=models.CharField(
                blank=True,
                help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.",
                max_length=255,
                verbose_name='repeated item link text'
            ),
        ),
    ]
