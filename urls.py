from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^view/$', views.public_view, name='view'),

    # League pages
    url(r'^league/editor/$', views.editor_league_list, name='league_manager'),
    url(r'^league/editor/(?P<pk>\d+)/\w*$', views.league_editor, name='league_editor'),
    url(r'^league/view/(?P<pk>\d+)/\w*$', views.league_view, name='league_view'),
    url(r'^league/add/$', views.add_league, name='add_league'),

    # Team pages
    url(r'^team/editor/$', views.editor_team_list, name='team_manager')
]
