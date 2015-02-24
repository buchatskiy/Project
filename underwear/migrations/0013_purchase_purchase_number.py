# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0012_auto_20150117_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_number',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
