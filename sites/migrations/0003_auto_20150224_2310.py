# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_site_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a_value', models.DecimalField(max_digits=5, decimal_places=2)),
                ('b_value', models.DecimalField(max_digits=5, decimal_places=2)),
                ('date', models.DateField(verbose_name=b'date published')),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='site',
            name='a_value',
        ),
        migrations.RemoveField(
            model_name='site',
            name='b_value',
        ),
        migrations.RemoveField(
            model_name='site',
            name='date',
        ),
    ]
