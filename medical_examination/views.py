
from django.shortcuts import render

from .forms import MedicalExaminationForm, MedicalExaminationListForm
from django.contrib.auth.decorators import login_required
from .models import MedicalExamination


@login_required
def medical_examination_view(request):
    if request.user.groups.filter(name__in=['lekarz']).exists():
        if request.method == 'POST':
            medical_examination = MedicalExaminationForm(request.user, request.POST, request.FILES)
            if medical_examination.is_valid():
                new_form = medical_examination.save(commit=False)
                new_form.doctor = request.user
                new_form.save()
        else:
            medical_examination = MedicalExaminationForm(request.user)
        return render(request, 'medical_examination_html/add.html', {'medical_examination': medical_examination, 'section': 'badania'})
    else:
        return render(request, 'medical_examination_html/list.html', {'section': 'badania'})


@login_required
def medical_examination_list_view(request):
    medical_examination_list = MedicalExamination.objects.filter(patient=request.user)
    return render(request, 'medical_examination_html/list.html', {'section': 'badania', 'badanie_list': medical_examination_list})


@login_required
def patient_history_list(request):
    if request.user.groups.filter(name__in=['lekarz']).exists():
        if request.method == 'POST':
            post_list = MedicalExaminationListForm(request.user, request.POST)
            print(post_list['patient'].value())
            history_list = MedicalExamination.objects.filter(patient=post_list['patient'].value())
        else:
            history_list = MedicalExaminationListForm(request.user)
        return render(request, 'medical_examination_html/history_list.html', {'history_list': history_list, 'section': 'test'})