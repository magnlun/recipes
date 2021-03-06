# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_models', '0006_auto_20160531_0700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='moment',
            name='extra_ingredients',
            field=models.ManyToManyField(blank=True, to='recipes_models.Ingredient'),
        ),
    ]
