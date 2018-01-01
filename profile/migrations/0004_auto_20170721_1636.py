# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_auto_20170718_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='PESEL',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='nomatch', regex='^\\d{11}$', message='PESEL musi składać się z 11 cyfr.')], max_length=11, blank=True, unique=True),
        ),
    ]
