# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
