from django.db import models
from django.contrib.auth.models import User

class Referral(models.Model):
    patient = models.ForeignKey(User, related_name='patient_referral')
    specialist = models.CharField(max_length=120)
    symptoms = models.CharField(max_length=500)
    key = models.CharField(max_length=10)
    reasons = models.CharField(max_length=500)
    examination =  models.CharField(max_length=500)

