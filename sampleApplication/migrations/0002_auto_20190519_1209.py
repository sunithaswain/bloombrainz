# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-19 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='upload',
            field=models.FileField(upload_to='documents/'),
        ),
    ]