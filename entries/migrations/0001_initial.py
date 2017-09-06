# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=96)),
                ('signature', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('slug', models.SlugField(editable=False)),
                ('session_key', models.CharField(max_length=40)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('modification_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
