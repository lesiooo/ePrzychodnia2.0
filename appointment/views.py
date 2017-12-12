from django.shortcuts import render
from .forms import AppointmentForm, InternalAppointmentForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.utils import timezone
from .models import Appointment
from django.contrib import messages
from django.contrib.auth.models import User
from badanie.forms import PatientFullName


@login_required
def appointment_add_view(request):
    appointment_list = Appointment.objects.filter(patient=request.user,
                                                  date_of_appointment__gte=timezone.now).order_by(
        'date_of_appointment')

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            new_form = appointment_form.save(commit=False)
            new_form.patient = request.user
            if new_form.date_of_appointment < timezone.now():
                messages.error(request, "Nie jest możliwe zapisanie się na datę wsteczną.")
                return render(request,  'appointment/add.html',
                  {'appointment_form': appointment_form,'section':'zapis',
                   'appointment_list': appointment_list})


            number_of_visites = Appointment.objects.filter(doctor=new_form.doctor,
                                                           date_of_appointment__day=new_form.date_of_appointment.day,
                                                           date_of_appointment__month=new_form.date_of_appointment.month,
                                                           date_of_appointment__year=new_form.date_of_appointment.year).count()
            if number_of_visites < 32:
                new_form.date_of_appointment += timedelta(hours=8, minutes=number_of_visites*15)
            else:
                days = 0
                while number_of_visites > 32:
                    days += 1
                    number_of_visites = Appointment.objects.filter(doctor=new_form.doctor,
                                                                   date_of_appointment__day=new_form.date_of_appointment.day+days,
                                                                   date_of_appointment__month=new_form.date_of_appointment.month,
                                                                   date_of_appointment__year=new_form.date_of_appointment.year).count()
                new_form.date_of_appointment += timedelta(days=days, hours=8, minutes=15*number_of_visites)

            daily_list = Appointment.objects.filter(doctor=new_form.doctor,
                                                                   date_of_appointment__day=new_form.date_of_appointment.day,
                                                                   date_of_appointment__month=new_form.date_of_appointment.month,
                                                                   date_of_appointment__year=new_form.date_of_appointment.year)


            for item in daily_list:
                if new_form.patient == item.patient:
                    messages.error(request, "Nie możesz zapisać się drugi raz na ten sam dzień.")
                    break
            else:
                new_form.save()
                messages.success(request, "Najbliższy termin badania to: " + str(new_form.date_of_appointment)[0:16])

    else:
        appointment_form = AppointmentForm()

    return render(request, 'appointment/add.html',
                  {'appointment_form': appointment_form,'section':'zapis',
                   'appointment_list': appointment_list})

@login_required
def internal_appointment_view(request):
    if request.method == 'POST':
        internal_appointment = InternalAppointmentForm(request.user, request.POST)
        if internal_appointment.is_valid():
            internal_appointment.save()
            messages.success(request, "Pomyślnie skierowano na badania wewnętrzne.")
    else:
        internal_appointment = InternalAppointmentForm(request.user)

    return render(request, 'appointment/internal_appointment.html', {'internal_appointment': internal_appointment, 'section':'zapis_wewnetrzny'})

@login_required
def list_of_patient(request):
    list_of_patient = Appointment.objects.filter(
                date_of_appointment__day=date.today().day,
                date_of_appointment__month=date.today().month,
                date_of_appointment__year=date.today().year,
                doctor=request.user)
    return render(request, 'appointment/list_of_patient.html', {'list_of_patient': list_of_patient})
