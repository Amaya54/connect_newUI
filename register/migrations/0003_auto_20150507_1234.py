# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20141130_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='fbUserName',
            field=models.CharField(default=b'guest', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='users',
            name='tags',
            field=models.CharField(default=b'$', max_length=1000),
            preserve_default=True,
        ),
    ]
