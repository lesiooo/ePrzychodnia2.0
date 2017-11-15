from django import forms
from .models import Badanie
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from appointment.models import Appointment
from datetime import date


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

    def __init__(self,user, *args,**kwargs):
        super(BadanieForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = (User.objects.filter(
            id__in=Appointment.objects.select_related('patient').values('patient').filter(date_of_appointment__day=date.today().day,
                                                                                          date_of_appointment__month=date.today().month,
                                                                                          date_of_appointment__year=date.today().year,
                                                                                           doctor=user)))
        self.fields['patient'].label = 'Pacjent'

    class Meta:
        model = Badanie
        fields = ('patient', 'file_of_medical_examination', 'notes')
        exclude = ('doctor',)
        labels = {
            'patient' : ('Pacjent'),
            'file_of_medical_examination' : ('Plik badania'),
            'notes' : ('Opis badania'),
            'date_of_medical_examination' : ('Data badania'),
        }


class BadanieListForm(forms.ModelForm):
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    def __init__(self, user, *args,**kwargs):
        super(BadanieListForm, self).__init__(*args,**kwargs)
        self.fields['patient'].queryset = (User.objects.filter(
            id__in=Appointment.objects.select_related('patient').values('patient').filter(date_of_appointment__day=date.today().day,
                                                                                          date_of_appointment__month=date.today().month,
                                                                                          date_of_appointment__year=date.today().year,
                                                                                          doctor=user)))
    class Meta:
        model = Badanie
        fields =('patient',)
        exclude = ('doctor', 'file_of_medical_examination', 'notes', 'date_of_medical_examination')