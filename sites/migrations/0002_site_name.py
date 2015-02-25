# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 2, 24, 22, 54, 24, 106263, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
