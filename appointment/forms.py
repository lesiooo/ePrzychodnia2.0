from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from badanie.forms import PatientFullName, DoctorFullName


class AppointmentForm(forms.ModelForm):
    doctor = User.objects.filter(groups__name='lekarz')

    class Meta:
        model = Appointment
        fields = ('doctor', 'date_of_appointment')
        exclude = ('patient', )



class AppointmentAdminForm(forms.ModelForm):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    class Meta:
        model = Appointment
        fields = ('patient','doctor', 'date_of_appointment')