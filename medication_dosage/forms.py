from django import forms
from badanie.forms import PatientFullName
from django.contrib.auth.models import User
from appointment.models import Appointment
from .models import MedicationDosage
from datetime import timedelta, date


class MedicationDosageForm(forms.ModelForm):
    patient = PatientFullName(User.objects.filter(groups__name='pacjent'))

    def __init__(self,user, *args,**kwargs):
        super(MedicationDosageForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = (User.objects.filter(
            id__in=Appointment.objects.select_related('patient').values('patient').filter(date_of_appointment__day=date.today().day,
                                                                                          date_of_appointment__month=date.today().month,
                                                                                          date_of_appointment__year=date.today().year,
                                                                                           doctor=user)))

    class Meta:
        model = MedicationDosage
        fields = ('patient','list_of_medicaments',)
        exclude = ('date',)



