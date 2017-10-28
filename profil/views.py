from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Profile
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request, 'profil/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid() and user_form.available_pesel():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_user.groups.add(Group.objects.get(name='pacjent'))
            #profil_dict = user_form.profil_dict()
            PESEL = user_form.clean_pesel()
            profile = Profile.objects.create(user=new_user, PESEL=PESEL, )
            return render(request, 'profil/register_done.html', {'new_user': new_user})
        elif user_form.available_pesel() == False:
            messages.error(request, message='PESEL jest już przez kogoś używany. Jeśli należy on do Ciebie, skontaktuj się z obsługą przychodni.')
        else:
            messages.error(request,message='Cos poszło nie tak, konto nie zostało utworzone.')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'profil/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'profil/edit.html', {'user_form': user_form, 'profile_form': profile_form})


def main_page(request):
    return render(request, 'profil/dashboard.html')
