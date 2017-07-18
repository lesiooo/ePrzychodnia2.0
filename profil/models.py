from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    PESEL = models.CharField(max_length=11,
                             validators=[RegexValidator(regex='^\d{11}$', message='PESEL musi składać się z 11 cyfr.', code='nomatch')],
                             blank=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True, )
    adres = models.CharField(max_length=100,null=True, blank=True)
    NIP = models.CharField(max_length=10,
                           validators=[RegexValidator(regex='^\d{10}$', message='NIP musi składać się z 10 cyfr.', code='nomatch')],
                           null=True, blank=True)

