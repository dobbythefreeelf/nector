# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ip',
        ),
        migrations.AddField(
            model_name='host',
            name='ipv4_address',
            field=models.GenericIPAddressField(default='0.0.0.0', protocol='ipv4'),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
