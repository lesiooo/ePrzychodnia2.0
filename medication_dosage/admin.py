from django.contrib import admin
from .models import MedicationDosage
from .forms import MedicationDosageAdminForm


class MedicationDosageAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'date', 'list_of_medicaments']

    def patient_name(self, instance):
        return instance.patient.get_full_name()

    form = MedicationDosageAdminForm

admin.site.register(MedicationDosage, MedicationDosageAdmin)
