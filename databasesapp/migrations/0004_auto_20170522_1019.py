# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databasesapp', '0003_detials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='fname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='lname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
    ]
