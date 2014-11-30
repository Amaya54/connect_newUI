# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='connectDetails',
            fields=[
                ('connectId', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('postId', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=200)),
                ('doc', models.DateTimeField(auto_now_add=True)),
                ('exchangeFlag', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
