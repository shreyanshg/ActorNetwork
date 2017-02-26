from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.actor_relations, name='actor_relations'),
    #url(r'^actors/(?P<search>.+)/$', views.search_actor, name='search_actor'),
    url(r'^actors$', views.get_actor, name='get_actor'),
    url(r'^movies$', views.get_movie, name='get_movie')
]
