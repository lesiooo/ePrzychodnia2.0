from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^dodaj/$', views.mediaction_dosage_view, name='medication_dosage_form'),
    url(r'^$', views.medication_dosage_list_view, name='medication_dosage_list'),
    url(r'^lista/$', views.medication_dosage_doctor_list, name='medication_dosage_doctor_list'),
]
