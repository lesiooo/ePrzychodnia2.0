# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='NIP',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='nomatch', message='NIP musi składać się z 10 cyfr.', regex='^\\d{10}$')], blank=True, null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PESEL',
            field=models.CharField(validators=[django.core.validators.RegexValidator(code='nomatch', message='PESEL musi składać się z 11 cyfr.', regex='^\\d{11}$')], blank=True, unique=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='profile',
            name='adres',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
