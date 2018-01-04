# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-04 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, default=None, null=True)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=7)),
                ('stock', models.IntegerField(default=0)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
