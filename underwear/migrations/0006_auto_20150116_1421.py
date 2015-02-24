# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0005_auto_20150116_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='post_office',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
