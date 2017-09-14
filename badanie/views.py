from django.shortcuts import render
from .forms import BadanieForm
from django.contrib.auth.decorators import login_required
from .models import Badanie


@login_required
def badanie_view(request):
    if request.user.groups.filter(name__in=['lekarz']).exists():
        if request.method == 'POST':
            badanie_form = BadanieForm(request.user, request.POST, request.FILES)
            if badanie_form.is_valid():
                new_form = badanie_form.save(commit=False)
                new_form.doctor = request.user
                new_form.save()
        else:
            badanie_form = BadanieForm(request.user)
        return render(request, 'badanie/add.html', {'badanie_form': badanie_form, 'section':'badania'})
    else:
        return render(request, 'badanie/list.html', {'section': 'badanie'})


@login_required
def badanie_list_view(request):
    badanie_list = Badanie.objects.filter(patient=request.user)
    return render(request, 'badanie/list.html', {'section': 'badanie', 'badanie_list': badanie_list})