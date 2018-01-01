# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20170721_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adres',
            new_name='street',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='NIP',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='city_code',
            field=models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(regex='^\\d{2}\\-\\d{3}', message='Niepoprawny format kodu "XX-XXX"', code='nomatch')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='house_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{{1,3}\\/{0,1}\\d*$', message='Zły format numeru "XXX/XXX"', code='nomatch')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='PESEL',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^\\d{11}$', message='PESEL musi składać się z 11 cyfr.', code='nomatch')], unique=True),
        ),
    ]
