from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'home$', views.index),
    url(r'logout', views.logout),
    url(r'process_hero', views.addHero),
    url(r'heropage', views.heropage),
    url(r'process_power', views.addPower),
    url(r'powerspage', views.powerspage),
    url(r'hero/(?P<number>\d+)$', views.onehero),
    url(r'addheropower', views.addheropower),
    url(r'hero/(?P<number>\d+)/like', views.likehero),
    url(r'hero/(?P<number>\d+)/unlike', views.unlikehero),
    ]
