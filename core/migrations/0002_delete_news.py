# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-22 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
    ]