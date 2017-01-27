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
        'leagues': league.season_set.all()
    }
    return core.render(request, 'gametracker/seasonManager.html', **context)
