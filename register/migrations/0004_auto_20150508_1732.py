# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150507_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='tags',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
    ]
