from django.contrib import admin
from .models import Badanie
from .forms import BadanieAdminForm

class BadanieAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name', 'file_of_medical_examination', 'notes', 'date_of_medical_examination']

    def doctor_name(self, instance):
        return 'dr {0}'.format(instance.doctor.get_full_name())

    def patient_name(self, instance):
        return instance.patient.get_full_name()

    form = BadanieAdminForm

admin.site.register(Badanie, BadanieAdmin)
