# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0011_auto_20150117_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='underwear',
            name='color',
            field=models.ForeignKey(blank=True, to='underwear.Color', null=True),
            preserve_default=True,
        ),
    ]
