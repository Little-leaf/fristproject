# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0002_advert'),
        ('users', '0002_recordbrowse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('cart_amount', models.IntegerField(default=0)),
                ('cart_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodInfo')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
