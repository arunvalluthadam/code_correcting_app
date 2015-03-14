# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questions', models.TextField(verbose_name='Questions')),
                ('function_name', models.CharField(max_length=200, verbose_name='Function Name')),
                ('test_function', models.CharField(max_length=200, verbose_name='Test Function')),
                ('expected_ans', models.CharField(max_length=200, verbose_name='Expected Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
