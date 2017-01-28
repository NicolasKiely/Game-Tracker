from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from common import core
from .models import League, Team


@login_required
def editor_list(request, pkLeague):
    ''' Top-level editor for leagues '''
    league = get_object_or_404(League, pk=pkLeague)
    context = {
        'title' : 'Team Manager',
        'league': league,
        'teams' : league.team_set.all()
    }
    return core.render(request, 'gametracker/teamManager.html', **context)


@login_required
def editor(request, pk):
    ''' Editor for team '''
    team = get_object_or_404(Team, pk=pk)
    context = {
        'title' : 'Team Editor',
        'team'  : team,
        'league': team.fkLeague
    }
    return core.render(request, 'gametracker/teamEditor.html', **context)


@login_required
def add(request):
    ''' Post for adding new team '''
    league_id = request.POST['league']
    name = request.POST['name']
    lname = request.POST['long']
    home = request.POST['home']

    league = get_object_or_404(League, pk=league_id)
    team = Team(name=name, longName=lname, home=home, fkLeague=league)
    team.save()

    return HttpResponseRedirect(
        reverse('gametracker:team_manager', args=(league_id,))
    )


@login_required
def edit(request):
    ''' Post for editting team data '''
    team = get_object_or_404(Team, pk=request.POST['teamid'])
    team.name = request.POST['name']
    team.lname = request.POST['long']
    team.home = request.POST['home']
    team.save()

    return HttpResponseRedirect(
        reverse('gametracker:team_manager', args=(team.fkLeague.id,))
    )


@login_required
def delete(request):
    ''' Post for deleting team data '''
    team = get_object_or_404(Team, pk=request.POST['teamid'])
    team.delete()

    return HttpResponseRedirect(
        reverse('gametracker:team_manager', args=(team.fkLeague.id,))
    )


def view(request, pk):
    ''' Public view of team '''
    pass

