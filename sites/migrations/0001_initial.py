# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'date published')),
                ('a_value', models.DecimalField(max_digits=5, decimal_places=2)),
                ('b_value', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
