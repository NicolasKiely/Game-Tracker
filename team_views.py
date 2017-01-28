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
    pass


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


def view(request, pk):
    ''' Public view of team '''
    pass

