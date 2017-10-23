from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReferralPDFForm


@login_required
def referral_pdf_view(request):
    if request.method == 'POST':
        referral_pdf = ReferralPDFForm(request.user, request.POST)
        #return render(request, 'referral/referral.html', {'referral_pdf': referral_pdf})
    else:
        referral_pdf = ReferralPDFForm(request.user)
    return render(request, 'referral/referralForm.html', {'referral_pdf': referral_pdf})