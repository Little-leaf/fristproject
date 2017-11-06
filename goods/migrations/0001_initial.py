# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cag_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goods_image', models.ImageField(upload_to='')),
                ('goods_visits', models.IntegerField(default=0)),
                ('goods_short', models.CharField(max_length=1000)),
                ('goods_desc', tinymce.models.HTMLField()),
                ('goods_units', models.CharField(max_length=20)),
                ('goods_sales', models.IntegerField(default=0)),
                ('goods_cag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
