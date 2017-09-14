from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.mediaction_dosage_view, name='dawkowanie_form'),
]
