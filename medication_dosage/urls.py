from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^add/$', views.mediaction_dosage_view, name='medication_dosage_form'),
    url(r'^$', views.medication_dosage_list_view, name='medication_dosage_list')
]
