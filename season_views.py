from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from common import core
from .models import League, Season


@login_required
def editor_list(request, pkLeague):
    ''' Top-level editor for leagues '''
    league = get_object_or_404(League, pk=pkLeague)
    context = {
        'title'  : 'Season Manager',
        'league' : league,
        'seasons': league.season_set.all()
    }
    return core.render(request, 'gametracker/seasonManager.html', **context)


@login_required
def editor(request, pk):
    ''' Editor for season '''
    pass


@login_required
def add(request):
    ''' Post for adding new season '''
    league_id = request.POST['league']
    sn_name = request.POST['name']

    league = get_object_or_404(League, pk=league_id)
    season = Season(name=sn_name, fkLeague=league)
    season.save()

    return HttpResponseRedirect(
        reverse('gametracker:season_manager', args=(league_id,))
    )


def view(request, pk):
    ''' Public view of season '''
    pass
