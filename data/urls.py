from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /wiki/
    url(r'^$', views.index, name='index'),
    # ex: /wiki/achievements/
    url(r'^achievements/$', views.achievements, name='allAchievements'),
    # ex: /wiki/achievements/social/
    url(r'^achievements/(?P<achievementTypeName>[a-z]+)/$', views.achievementType, name='achievementType'),
    # ex: /wiki/achievements/social/5/
    url(r'^achievements/(?P<achievementType_id>[0-9]+)/(?P<achievement_id>[0-9]+)/$', views.achievement,
        name='achievement'),
    # ex: /wiki/achievements/social/offer/
    url(r'^achievements/(?P<achievementType_id>[0-9]+)/offer/$', views.offerAchievement, name='offerAchievement'),
]
