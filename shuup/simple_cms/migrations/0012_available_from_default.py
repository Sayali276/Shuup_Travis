# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-17 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_simple_cms', '0011_open_graph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='available_from',
            field=models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, help_text='Set an available from date to restrict the page to be available only after a certain date and time. This is useful for pages describing sales campaigns or other time-sensitive pages.', null=True, verbose_name='available from'),
        ),
    ]