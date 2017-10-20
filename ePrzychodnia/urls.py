from django.conf.urls import include, url
from django.contrib import admin
from profil import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profil/', include('profil.urls')),
    url(r'^badanie/', include('badanie.urls')),
    url(r'^$', 'profil.views.main_page'),
    url(r'^zapis/', include('appointment.urls')),
    url(r'^dawkowanie/', include('medication_dosage.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
