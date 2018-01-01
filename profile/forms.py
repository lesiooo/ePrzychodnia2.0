from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.validators import RegexValidator


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')
    PESEL = forms.CharField(max_length=11, validators=[RegexValidator(regex='^\d{11}$', message='PESEL musi składać się z 11 cyfr.', code='nomatch')])
    city = forms.CharField(max_length=100)
    street = forms.CharField(max_length=100)
    city_code = forms.CharField(max_length=6, validators=[RegexValidator(regex='^\d{2}\-\d{3}', message='Niepoprawny format kodu "XX-XXX"', code='nomatch')])
    house_number = forms.CharField(max_length=10,validators=[RegexValidator(regex='^\d{1,3}\/{0,1}\d*$', message='Zły format numeru "XXX/XXX"', code='nomatch')])
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        widgets = {'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'})}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła różnią się.')
        return cd['password2']

    def available_pesel(self):
        cd = self.cleaned_data.get('PESEL')
        if Profile.objects.filter(PESEL=cd).exists():
            return False
        else:
            return True
    def clean_email(self):
        cd = self.cleaned_data.get('email')
        if User.objects.filter(email=cd).exists():
            raise forms.ValidationError('Adres email jest już używany.')
        return cd

    def clean_pesel(self):
        cd = self.cleaned_data.get('PESEL')
        return cd

    def clean_city(self):
        cd = self.cleaned_data.get('city')
        return cd

    def clean_street(self):
        cd = self.cleaned_data.get('street')
        return cd

    def clean_city_code(self):
        cd = self.cleaned_data.get('city_code')
        return cd

    def clean_house_number(self):
        cd = self.cleaned_data.get('house_number')
        return cd

    def clean_date_of_birth(self):
        cd = self.cleaned_data.get('date_of_birth')
        return cd

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'street', 'city_code', 'house_number')

