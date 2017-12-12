from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from badanie.forms import PatientFullName, DoctorFullName
from django.utils.translation import ugettext_lazy as _
from datetime import timedelta, date


class AppointmentForm(forms.ModelForm):

    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    def __init__(self, *args,**kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].label = 'Doktor'


    class Meta:
        model = Appointment
        exclude = ('patient', 'notes')
        widgets = {'date_of_appointment':forms.DateInput(attrs={'class': 'datepicker'})}
        labels = {
            'date_of_appointment' : _('Data wizyty'),
        }


class AppointmentAdminForm(forms.ModelForm):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    class Meta:
        model = Appointment
        labels = {
            'patient' : _('Pacjent'),
            'doctor': _('Lekarz'),
            'date_of_appointment': _('Data wizyty'),
        }
        fields = ('patient','doctor', 'date_of_appointment', 'notes')


class InternalAppointmentForm(forms.ModelForm):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    def __init__(self, user, *args, **kwargs):
        super(InternalAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = (User.objects.filter(
            id__in=Appointment.objects.select_related('patient').values('patient').filter(
                date_of_appointment__day=date.today().day,
                date_of_appointment__month=date.today().month,
                date_of_appointment__year=date.today().year,
                doctor=user)))
        self.fields['patient'].label = 'pacjent'

    class Meta:
        model = Appointment
        fields = ('patient', 'doctor', 'date_of_appointment', 'notes')
        widgets = {'date_of_appointment': forms.DateInput(attrs={'class': 'datepicker'})}
