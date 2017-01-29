from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from common import core
from .models import Match, Participation, Season


@login_required
def editor_list(request, pkSeason):
    ''' Top-level editor for matches '''
    season = get_object_or_404(Season, pk=pkSeason)
    context = {
        'title'  : 'Schedule Manager',
        'season' : season,
        'matches': season.match_set.all()
    }
    return core.render(request, 'gametracker/matchManager.html', **context)
