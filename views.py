from common import core
from .models import League


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

def editor_league_list(request):
    ''' Top-level editor for leagues '''
    context = {
    }
    return core.render(request, 'gametracker/leagueManager.html', **context)


def editor_league(request):
    pass


def view_league(request):
    pass


def edit_league(request):
    pass


def add_league(request):
    pass


def editor_team_list(request):
    pass
