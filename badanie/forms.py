from django import forms
from .models import Badanie
from django.forms import ModelChoiceField
from django.contrib.auth.models import User



class DoctorFullName(ModelChoiceField):
    def label_from_instance(self, instance):
        return 'dr {0}'.format(str(instance.get_full_name()))

class PatientFullName(ModelChoiceField):
    def label_from_instance(self, instance):
        return '{0} {1}'.format(str(instance.get_full_name()), str(instance.profile.PESEL))

class BadanieAdminForm(forms.ModelForm, ):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    class Meta:
        model = Badanie
        fields = ('doctor','patient','file_of_medical_examination', 'notes', 'date_of_medical_examination')


class BadanieForm(forms.ModelForm):
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    class Meta:
        model = Badanie
        fields = ('patient', 'file_of_medical_examination', 'notes')
        exclude = ('doctor',)

