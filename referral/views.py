from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .forms import ReferralPDFForm
from profil.models import Profile


@login_required
def referral_pdf_view(request):
    if request.method == 'POST':
        data = request.POST
        personal_information = personal_data(data['patient'])
        #return render(request, 'referral/referral2.html', {'referral_pdf': data, 'personal_information':personal_information})
        html = render_to_string('referral/referral.html', {'referral_pdf': data, 'personal_information':personal_information})
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'skierowanie.pdf'
        weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS('static/css/referral_pdf.css')])
        return response
    else:
        referral_pdf = ReferralPDFForm(request.user)
        return render(request, 'referral/referralForm.html', {'referral_pdf': referral_pdf})


def personal_data(profile):
    patient_name = User.objects.filter(id=profile)[0].get_full_name()
    pesel = (Profile.objects.filter(user_id=profile).values('PESEL')[0])['PESEL']
    city = (Profile.objects.filter(user_id=profile).values('city')[0])['city']
    house_number = (Profile.objects.filter(user_id=profile).values('house_number')[0])['house_number']
    city_code = (Profile.objects.filter(user_id=profile).values('city_code')[0])['city_code']
    street = (Profile.objects.filter(user_id=profile).values('street')[0])['street']
    personal_data = {'patient_name': patient_name, 'PESEL': pesel,
                     'adres': str(street + ' ' + house_number + ', ' + city_code + ' '+ city)}
    return personal_data