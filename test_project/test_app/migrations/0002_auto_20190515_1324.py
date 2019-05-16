# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-15 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testgroup',
            name='restriction_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_app_testgroup_restrictions', to='contenttypes.ContentType', verbose_name='restriction content type id'),
        ),
    ]
