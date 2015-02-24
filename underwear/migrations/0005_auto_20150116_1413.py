# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0004_auto_20150116_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='post_office',
            field=models.DecimalField(max_digits=3, decimal_places=0),
            preserve_default=True,
        ),
    ]
