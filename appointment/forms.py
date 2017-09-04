from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from badanie.forms import PatientFullName, DoctorFullName
from django.contrib.admin.widgets import AdminDateWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class AppointmentForm(forms.ModelForm):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))

    class Meta:
        model = Appointment
        exclude = ('patient', )
        widgets = {'date_of_appointment':forms.DateInput(attrs={'class': 'datepicker'})}



class AppointmentAdminForm(forms.ModelForm):
    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    class Meta:
        model = Appointment
        fields = ('patient','doctor', 'date_of_appointment')
