# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0007_auto_20150117_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='underwear',
            options={'ordering': ['-availableM', 'series']},
        ),
        migrations.RenameField(
            model_name='underwear',
            old_name='available',
            new_name='availableM',
        ),
    ]
