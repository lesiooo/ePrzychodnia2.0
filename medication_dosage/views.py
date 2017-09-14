from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MedicationDosageForm
from django.contrib import messages


@login_required
def mediaction_dosage_view(request):
    if request.method =='POST':
        mediaction_dosage_form = MedicationDosageForm(request.user ,request.POST)
        if mediaction_dosage_form.is_valid():
            mediaction_dosage_form.save()
            messages.success(request, 'Poprawnie dodałeś wytyczne dla pacjenta')
        else:
            messages.error(request, 'coś poszło nie tak.')
    else:
        mediaction_dosage_form = MedicationDosageForm(request.user)
    return render(request, 'medication_dosage/add.html', {'medication_dosage_form':mediaction_dosage_form, 'section': 'dawkowanie'})




# Create your views here.
