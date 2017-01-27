from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from common import core
from .models import League


@login_required
def editor_list(request):
    ''' Top-level editor for leagues '''
    context = {
        'title'  : 'League Manager',
        'leagues': League.objects.all()
    }
    return core.render(request, 'gametracker/leagueManager.html', **context)


@login_required
def add(request):
    ''' Post for adding league '''
    lgName = request.POST['name']
    lgHiWins = True if 'hiwins' in request.POST else False

    league = League(name=lgName, highWins=lgHiWins)
    league.save()

    return HttpResponseRedirect(
        reverse('gametracker:league_manager')
    )


@login_required
def editor(request, pk):
    context = {
        'title': 'League',
        'league': get_object_or_404(League, pk=pk)
    }
    return core.render(request, 'gametracker/leagueEditor.html', **context)


def view(request, pk):
    context = {
        'title': 'League',
        'league': get_object_or_404(League, pk=pk)
    }
    return core.render(request, 'gametracker/viewLeague.html', **context)


@login_required
def edit(request):
    pass
