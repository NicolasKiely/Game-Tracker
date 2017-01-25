from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from common import core
from .models import League


@login_required
def dashboard(request):
    ''' Admin dashboard for gametracker '''
    context = {
        'title'  : 'Game Tracker Dashboard',
        'leagues': League.objects.all()
    }
    return core.render(request, 'gametracker/dashboard.html', **context)


def public_view(request):
    ''' Public page for gametracker '''
    pass


@login_required
def editor_league_list(request):
    ''' Top-level editor for leagues '''
    context = {
        'title'  : 'League Manager',
        'leagues': League.objects.all()
    }
    return core.render(request, 'gametracker/leagueManager.html', **context)


@login_required
def add_league(request):
    ''' Post for adding league '''
    lgName = request.POST['name']
    lgHiWins = True if 'hiwins' in request.POST else False

    league = League(name=lgName, highWins=lgHiWins)
    league.save()

    return HttpResponseRedirect(
        reverse('gametracker:league_manager')
    )


@login_required
def league_editor(request, pk):
    pass


def league_view(request, pk):
    pass


@login_required
def edit_league(request):
    pass


@login_required
def editor_team_list(request):
    pass
