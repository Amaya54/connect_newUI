# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='postDetails',
            fields=[
                ('postId', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('userId', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('dop', models.DateTimeField(auto_now_add=True)),
                ('filterBy', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
