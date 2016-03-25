from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wiki/', include('data.urls')),
    url(r'^profile/', include('userprofile.urlsApi')),
]