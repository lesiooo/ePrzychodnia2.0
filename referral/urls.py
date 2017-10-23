from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.referral_pdf_view, name='skierowanie'),

]