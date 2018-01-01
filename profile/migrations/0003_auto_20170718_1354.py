# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20170710_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='PESEL',
            field=models.CharField(max_length=11, blank=True, validators=[django.core.validators.RegexValidator(message='PESEL musi składać się z 11 cyfr.', regex='^\\d{11}$', code='nomatch')]),
        ),
    ]
