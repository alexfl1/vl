# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_remove_nodes_node_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodes',
            name='node_code',
            field=models.IntegerField(default=0),
        ),
    ]
