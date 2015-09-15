# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('koier', '0002_auto_20150912_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='koie',
            name='koordinater',
        ),
        migrations.AddField(
            model_name='koie',
            name='lat',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='koie',
            name='lon',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rapport',
            name='dato',
            field=models.DateField(default=datetime.datetime(2015, 9, 14, 14, 18, 29, 492949, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='koie',
            field=models.ForeignKey(to='koier.Koie'),
        ),
    ]
