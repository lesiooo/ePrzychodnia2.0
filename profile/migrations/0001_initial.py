# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('PESEL', models.CharField(validators=[django.core.validators.RegexValidator(message='PESEL musi składać się z 11 cyfr.', regex='^\\d{11}$', code='nomatch')], max_length=11, unique=True)),
                ('date_of_birth', models.DateField()),
                ('adres', models.CharField(max_length=100)),
                ('NIP', models.CharField(validators=[django.core.validators.RegexValidator(message='NIP musi składać się z 10 cyfr.', regex='^\\d{10}$', code='nomatch')], max_length=10, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
