from django.conf.urls import url

from authorization import views

urlpatterns = [

    # ex: /login/
    url(r'^$', views.index, name='index'),

    #ex: /login/register/
    url(r'^register/$', views.register, name='register'),

    #ex: /login/restorepassword
    url(r'^restorepassword/$', views.restorePassword, name='restorePassword')
]