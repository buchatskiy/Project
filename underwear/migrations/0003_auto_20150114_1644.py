# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('underwear', '0002_auto_20150111_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('totalprice', models.FloatField()),
                ('phone_number', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('post_office', models.IntegerField()),
                ('divisions', models.CharField(max_length=1, choices=[(b'a', b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb6\xd0\xbe\xd0\xbc'), (b'b', b'100% \xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x83 \xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x82 \xd0\x91\xd0\xb0\xd0\xbd\xd0\xba\xd0\xb0*')])),
                ('underwear', models.ManyToManyField(to='underwear.Underwear')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('totalprice', models.FloatField()),
                ('phone_number', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='underwear',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
        migrations.AlterModelOptions(
            name='underwear',
            options={'ordering': ['-available', 'series']},
        ),
    ]
