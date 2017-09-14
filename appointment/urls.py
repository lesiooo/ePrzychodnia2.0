from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.appointment_add_view, name='zapis_do_lekarza'),
]
