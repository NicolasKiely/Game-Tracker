from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from common import core
from .models import Match, Participation, Season
from datetime import datetime 


@login_required
def editor_list(request, pkSeason):
    ''' Top-level editor for matches '''
    season = get_object_or_404(Season, pk=pkSeason)
    context = {
        'title'  : 'Schedule Manager',
        'season' : season,
        'matches': season.match_set.all(),
        'form'   : {
            'action': 'gametracker:add_match',
            'fields': Match(round=1, fkSeason=season, date=datetime.today()).to_form_fields()
        }
    }
    return core.render(request, 'gametracker/matchManager.html', **context)

@login_required
def add(request):
    ''' Post handler for adding team '''
    pass
