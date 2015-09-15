# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Koie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('navn', models.CharField(max_length=30)),
                ('sengeplasser', models.IntegerField(verbose_name=20)),
                ('skaderapport', models.CharField(max_length=200)),
            ],
        ),
    ]
