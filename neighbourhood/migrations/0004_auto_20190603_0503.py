# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-03 05:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_auto_20190603_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='neighbourhood',
            new_name='location',
        ),
    ]