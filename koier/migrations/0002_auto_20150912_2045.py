# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('dato', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Dugnad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dato', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skaderapport', models.CharField(max_length=200)),
                ('vedstatus', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='koie',
            name='skaderapport',
        ),
        migrations.AddField(
            model_name='koie',
            name='koordinater',
            field=models.FloatField(default=54.222),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='koie',
            name='sengeplasser',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='rapport',
            name='koie',
            field=models.ForeignKey(to='koier.Koie'),
        ),
        migrations.AddField(
            model_name='dugnad',
            name='koie',
            field=models.ForeignKey(to='koier.Koie'),
        ),
        migrations.AddField(
            model_name='booking',
            name='koie',
            field=models.ForeignKey(to='koier.Koie'),
        ),
    ]
