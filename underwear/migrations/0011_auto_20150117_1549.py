# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0010_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='underwear',
            options={'ordering': ['-availableM', 'series']},
        ),
        migrations.AddField(
            model_name='underwear',
            name='color',
            field=models.ForeignKey(default=1, to='underwear.Color'),
            preserve_default=False,
        ),
    ]
