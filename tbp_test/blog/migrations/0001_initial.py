# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-28 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('upa', models.IntegerField(default=0)),
                ('pda', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
