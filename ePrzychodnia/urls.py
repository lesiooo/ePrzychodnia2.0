from django.conf.urls import include, url
from django.contrib import admin
from profile import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profil/', include('profile.urls')),
    url(r'^badanie/', include('medical_examination.urls')),
    url(r'^$', 'profile.views.main_page'),
    url(r'^zapis/', include('appointment.urls')),
    url(r'^dawkowanie/', include('medication_dosage.urls')),
    url(r'^skierowanie/', include('referral.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

