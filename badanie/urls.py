from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^add/$', views.badanie_view, name='badanie_add'),
    url(r'^list/$', views.badanie_list_view, name='list'),

]