# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20141129_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='contactNo',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
