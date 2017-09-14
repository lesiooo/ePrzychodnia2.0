from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MedicationDosage(models.Model):
    patient = models.ForeignKey(User, related_name='patient__medicationdosage')
    date = models.DateField(auto_now=True)
    list_of_medicaments = models.TextField()


