# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-15 00:04
from __future__ import unicode_literals

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ('maasserver', '0172_partition_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='install_kvm',
            field=models.BooleanField(default=False),
        ),
    ]
