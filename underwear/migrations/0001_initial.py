# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('totalprice', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Underwear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idu', models.CharField(max_length=30)),
                ('available', models.IntegerField()),
                ('series', models.ForeignKey(to='underwear.Series')),
            ],
            options={
                'ordering': ['series'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='purchase',
            name='underwear',
            field=models.ManyToManyField(to='underwear.Underwear'),
            preserve_default=True,
        ),
    ]
