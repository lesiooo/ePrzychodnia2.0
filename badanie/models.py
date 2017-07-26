from django.db import models
from django.utils import timezone
from django.conf import settings
from profil.models import Profile
from django.contrib.auth.models import User


def generate_filename(instance, filename):
    return 'files/{0}_{1}_{2}/{3}'.format(str(instance.patient.first_name)
                                          , str(instance.patient.last_name), str(instance.patient.profile.PESEL), filename)


class Badanie(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='doctor')
    patient = models.ForeignKey(User, related_name='patient')
    date_of_medical_examination = models.DateField(default=timezone.now)
    file_of_medical_examination = models.FileField(blank=True, upload_to=generate_filename)
    notes = models.TextField()
