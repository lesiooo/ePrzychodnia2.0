from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')




    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Hasła różnią się.')
            return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'PESEL', 'date_of_birth', 'NIP', 'adres')

