# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_auto_20171026_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='house_number',
            field=models.CharField(max_length=10, blank=True, validators=[django.core.validators.RegexValidator(regex='^\\d{1,3}\\/{0,1}\\d*$', message='Zły format numeru "XXX/XXX"', code='nomatch')]),
        ),
    ]
