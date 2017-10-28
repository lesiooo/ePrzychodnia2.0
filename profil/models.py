from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    PESEL = models.CharField(max_length=11,
                             validators=[RegexValidator(regex='^\d{11}$', message='PESEL musi składać się z 11 cyfr.', code='nomatch')],
                             unique=True, blank=False)
    date_of_birth = models.DateField(null=True, blank=True, )
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, validators=[RegexValidator(regex='^\d{{1,3}\/{0,1}\d*$', message='Zły format numeru "XXX/XXX"', code='nomatch')])
    city_code = models.CharField(max_length=6, blank=True, validators=[RegexValidator(regex='^\d{2}\-\d{3}', message='Niepoprawny format kodu "XX-XXX"', code='nomatch')])

