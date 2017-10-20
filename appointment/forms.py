from django import forms
from .models import Appointment
from django.contrib.auth.models import User
from badanie.forms import PatientFullName, DoctorFullName
from django.contrib.admin.widgets import AdminDateWidget
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.utils.translation import ugettext_lazy as _

class AppointmentForm(forms.ModelForm):

    def __init__(self, *args,**kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].label = 'Doktor'

    doctor = DoctorFullName(User.objects.filter(groups__name='lekarz'))

    class Meta:
        model = Appointment
        exclude = ('patient', )
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
        fields = ('patient','doctor', 'date_of_appointment')
