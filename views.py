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
def editor_team_list(request):
    pass
