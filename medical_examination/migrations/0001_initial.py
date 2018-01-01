# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalExamination',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('date_of_medical_examination', models.DateField(default=django.utils.timezone.now)),
                ('file_of_medical_examination', models.FileField(upload_to='files/', blank=True)),
                ('notes', models.TextField()),
                ('doctor', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='patient')),
            ],
        ),
    ]
