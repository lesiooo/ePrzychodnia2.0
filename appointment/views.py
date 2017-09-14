from django.shortcuts import render
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.utils import timezone
from .models import Appointment
from django.contrib import messages

@login_required
def appointment_add_view(request):
    appointment_list = Appointment.objects.filter(patient=request.user, date_of_appointment__gte=timezone.now).order_by(
        'date_of_appointment')

    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            new_form = appointment_form.save(commit=False)
            new_form.patient = request.user
            number_of_visites = Appointment.objects.filter(doctor=new_form.doctor,
                                                           date_of_appointment__day=new_form.date_of_appointment.day,
                                                           date_of_appointment__month=new_form.date_of_appointment.month,
                                                           date_of_appointment__year=new_form.date_of_appointment.year).count()
            if number_of_visites < 2:
                new_form.date_of_appointment += timedelta(hours=8, minutes=number_of_visites*15)
            else:
                days = 0
                while number_of_visites > 2:
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
                  {'appointment_form': appointment_form,'section':'zapis', 'appointment_list': appointment_list})


# Create your views here.
