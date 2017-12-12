from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.appointment_add_view, name='zapis_do_lekarza'),
    url(r'^wewnetrzne/$', views.internal_appointment_view, name='skierowanie_wewnetrzne' ),
    url(r'^przyjecia/$', views.list_of_patient, name='patient_list')
]
