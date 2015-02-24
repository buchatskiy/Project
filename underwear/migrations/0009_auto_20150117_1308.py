# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0008_auto_20150117_1307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='underwear',
            options={'ordering': ['-availableM', '-availableL', '-availableXL', 'series']},
        ),
        migrations.AddField(
            model_name='underwear',
            name='availableL',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='underwear',
            name='availableXL',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
