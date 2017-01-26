from django.conf.urls import url
from . import views
from . import league_views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^view/$', views.public_view, name='view'),

    # League pages
    url(r'^league/editor/$', league_views.editor_list, name='league_manager'),
    url(r'^league/editor/(?P<pk>\d+)/\w*$', league_views.editor, name='league_editor'),
    url(r'^league/view/(?P<pk>\d+)/\w*$', league_views.view, name='league_view'),
    url(r'^league/add/$', league_views.add, name='add_league'),

    # Team pages
    url(r'^team/editor/$', views.editor_team_list, name='team_manager')
]
