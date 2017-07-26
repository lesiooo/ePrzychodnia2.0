from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import BadanieForm, DoctorFullName
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


@login_required
def badanie_view(request):
    if request.method == 'POST':
        badanie_form = BadanieForm(request.POST, request.FILES)
        if badanie_form.is_valid():
            new_form = badanie_form.save(commit=False)
            new_form.doctor = request.user
            new_form.save()

    else:
        badanie_form = BadanieForm()
    return render(request, 'badanie/add.html', {'badanie_form': badanie_form, 'section':'badania'})
