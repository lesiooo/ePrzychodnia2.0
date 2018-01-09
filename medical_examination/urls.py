from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^add/$', views.medical_examination_view, name='badanie_add'),
    url(r'^list/$', views.medical_examination_list_view, name='list'),
    url(r'^historia/$', views.patient_medical_examination_history_list, name='history_list')

]