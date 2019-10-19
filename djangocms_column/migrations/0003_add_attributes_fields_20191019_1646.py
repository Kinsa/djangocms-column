# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-19 20:46
from __future__ import unicode_literals

from django.db import migrations
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_column', '0002_auto_20160915_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict),
        ),
        migrations.AddField(
            model_name='multicolumns',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict),
        ),
    ]