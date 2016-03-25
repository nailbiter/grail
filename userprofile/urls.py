from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /profile/172345
    url(r'^(?P<profileId>[0-9]+)/$', views.profile_by_id, name='profileById'),
    # ex: /profile/orion
    url(r'^(?P<profileName>[A-Za-z_.]+)/$', views.profile_by_name, name='profileByName'),
]