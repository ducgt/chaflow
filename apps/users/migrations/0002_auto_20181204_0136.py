# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-12-03 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('crm_table_list', '可以查看每张表里所有的数据'), ('crm_table_list_view', '可以访问表里每条数据的修改页'), ('crm_table_list_change', '可以对表里的每条数据进行修改'), ('crm_table_obj_add_view', '可以访问每张表的数据增加页'), ('crm_table_obj_add', '可以对每张表进行数据添加'))},
        ),
    ]