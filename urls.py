from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^view/$', views.public_view, name='view'),
    url(r'^league/editor/$', views.editor_league_list, name='league_manager'),
    url(r'^team/editor/$', views.editor_team_list, name='team_manager')
]
