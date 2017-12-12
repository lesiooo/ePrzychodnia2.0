from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MedicationDosageForm, MedicationDosageListForm
from django.contrib import messages
from .models import MedicationDosage


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

@login_required
def medication_dosage_list_view(request):
    medication_dosage_list = MedicationDosage.objects.filter(patient=request.user).order_by('date')
    return render(request, 'medication_dosage/list.html', {'medication_dosage_list':medication_dosage_list, 'section': 'dawkowanie'})

@login_required
def medication_dosage_doctor_list(request):
    if request.method == 'POST':
        post_data = MedicationDosageListForm(request.user, request.POST)
        medication_list = MedicationDosage.objects.filter(patient=post_data['patient'].value())
    else:
        medication_list = MedicationDosageListForm(request.user)

    return render(request, 'medication_dosage/doctor_list.html', {'section': 'dawkowanie', 'medication_list': medication_list})