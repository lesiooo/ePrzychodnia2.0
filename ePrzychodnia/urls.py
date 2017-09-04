from django.conf.urls import include, url
from django.contrib import admin
from profil import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profil/', include('profil.urls')),
    url(r'^badanie/', include('badanie.urls')),
    url(r'^$', 'profil.views.main_page'),
    url(r'^zapis/', include('appointment.urls')),
]
