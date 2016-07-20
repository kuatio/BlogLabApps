# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160718_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imgportada',
            old_name='url',
            new_name='image',
        ),
        migrations.AddField(
            model_name='articulo',
            name='imageportada',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.imgportada'),
        ),
    ]
