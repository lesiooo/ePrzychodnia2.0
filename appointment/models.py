from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='appointment_patient')
    doctor = models.ForeignKey(User, related_name='appointment_doctor')
    date_of_appointment = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True, null=True)
