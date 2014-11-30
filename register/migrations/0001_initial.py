# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('userId', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('contactNo', models.CharField(max_length=200)),
                ('doj', models.DateTimeField(auto_now_add=True)),
                ('flags', models.CharField(max_length=3)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
