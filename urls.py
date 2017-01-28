from django.conf.urls import url
from . import views
from . import league_views
from . import season_views
from . import team_views


urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^view/$', views.public_view, name='view'),

    # League pages
    url(r'^league/editor/$', league_views.editor_list, name='league_manager'),
    url(r'^league/editor/(?P<pk>\d+)/\w*$', league_views.editor, name='league_editor'),
    url(r'^league/view/(?P<pk>\d+)/\w*$', league_views.view, name='league_view'),
    url(r'^league/add/$', league_views.add, name='add_league'),

    # Season pages
    url(r'^league/(?P<pkLeague>\d+)/season/editor/$',
        season_views.editor_list, name='season_manager'),
    url(r'^season/editor/(?P<pk>\d+)/\w*$', season_views.editor, name='season_editor'),
    url(r'^season/view/(?P<pk>\d+)/\w*$', season_views.view, name='season_view'),
    url(r'^season/add/$', season_views.add, name='add_season'),
    url(r'^season/edit/$', season_views.edit, name='edit_season'),
    url(r'^season/delete/$', season_views.delete, name='delete_season'),

    # Team pages
    url(r'^league/(?P<pkLeague>\d+)/team/editor/$',
        team_views.editor_list, name='team_manager'),
    url(r'^team/editor/(?P<pk>\d+)/\w*$', team_views.editor, name='team_editor'),
    url(r'^team/view/(?P<pk>\d+)/\w*$', team_views.view, name='team_view'),
    url(r'^team/add/$', team_views.add, name='add_team'),
    url(r'^team/edit/$', team_views.edit, name='edit_team'),
    url(r'^team/delete/$', team_views.delete, name='delete_team')
]
