# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_recordbrowse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('detail_name', models.CharField(max_length=50)),
                ('detail_price', models.IntegerField()),
                ('detail_amount', models.IntegerField()),
                ('detail_unit', models.CharField(max_length=20)),
                ('detail_img', models.ImageField(upload_to='')),
                ('detail_goodsid', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('set_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('order_code', models.CharField(max_length=11)),
                ('order_addr', models.CharField(max_length=50)),
                ('order_recv', models.CharField(max_length=10)),
                ('order_status', models.SmallIntegerField(choices=[(1, '待付款'), (2, '待发货'), (3, '待收货'), (4, '已完成')], default=1)),
                ('order_pay', models.SmallIntegerField(choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝支付'), (4, '银联支付')], default=1)),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='detail',
            name='detail_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]
