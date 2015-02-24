# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0006_auto_20150116_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='underwear',
            name='sizes',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
