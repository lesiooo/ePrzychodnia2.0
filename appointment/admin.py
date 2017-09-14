from django.contrib import admin
from .models import Appointment
from .forms import AppointmentAdminForm

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'date_of_appointment']

    def doctor_name(self, instance):
        return 'dr {0}'.format(instance.doctor.get_full_name())

    def patient_name(self, instance):
        return instance.patient.get_full_name()

    form = AppointmentAdminForm

admin.site.register(Appointment, AppointmentAdmin)