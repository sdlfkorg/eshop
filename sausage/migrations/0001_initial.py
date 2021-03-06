# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分類名稱')),
            ],
            options={
                'verbose_name_plural': '標籤',
                'verbose_name': '標籤',
            },
        ),
        migrations.CreateModel(
            name='Sausage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='商品名稱')),
                ('desription', models.TextField(blank=True, default='', verbose_name='商品敘述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='新增時間')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('published', models.DateTimeField(null=True, verbose_name='上架時間')),
                ('original_price', models.PositiveIntegerField(default=0, verbose_name='原價')),
                ('current_price', models.PositiveIntegerField(default=0, verbose_name='售價')),
                ('place_of_origin', models.TextField(blank=True, default='', verbose_name='產地')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sausage.Category', verbose_name='商品分類')),
            ],
            options={
                'verbose_name_plural': '香腸',
                'verbose_name': '香腸',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='標籤名稱')),
            ],
            options={
                'verbose_name_plural': '標籤',
                'verbose_name': '標籤',
            },
        ),
        migrations.AddField(
            model_name='sausage',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sausage.Tag', verbose_name='標籤'),
        ),
    ]
