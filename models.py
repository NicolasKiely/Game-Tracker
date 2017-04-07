from django.db import models
from django.core.urlresolvers import reverse
from common.core import view_link, edit_link
from django.core.exceptions import ObjectDoesNotExist


# Sports/Game league
class League(models.Model):
    # Unique name of sport
    name     = models.CharField('League', max_length=64, unique=True)
    # Whether a high score wins
    highWins = models.BooleanField('High Score Wins', default=True)

    def edit_link(self):
        return edit_link('gametracker:league_editor', (self.pk,))

    def view_link(self):
        return view_link('gametracker:league_view', (self.pk,), self.name)

    def manager_link(self):
        link_url = reverse('gametracker:league_editor', args=(self.id,))
        return '<a href="'+ link_url +'">League: '+ self.name +'</a>'


# Team in a league
class Team(models.Model):
    # Unique short/abbreviated name of team
    name     = models.CharField('Team', max_length=16, unique=True)
    # Long descriptive name
    longName = models.CharField('Long Name', max_length=64)
    # Optional home region/city/state
    home     = models.CharField('Team Home', max_length=64)
    # League team participates in
    fkLeague = models.ForeignKey(League, on_delete=models.CASCADE)

    def edit_link(self):
        return edit_link('gametracker:team_editor', (self.pk,))

    def view_link(self):
        ''' Returns anchor link for view '''
        return view_link('gametracker:team_view', (self.pk,), self.longName)

    def nav_link(self):
        return self.fkLeague.manager_link() +' | '+ self.view_link()

    def to_form_fields(self):
        return [
            {'label': 'Name:'     , 'name': 'name'    , 'value': self.name},
            {'label': 'Long Name:', 'name': 'long'    , 'value': self.longName},
            {'label': 'Home:'     , 'name': 'home'    , 'value': self.home},
            {'type' : 'hidden'    , 'name': 'teamid'  , 'value': self.id},
            {'type' : 'hidden'    , 'name': 'leagueid', 'value': self.fkLeague.id}
        ]


# Season or time period of sequential matches in league
class Season(models.Model):
    # Name of season (eg Winter)
    name     = models.CharField('Season', max_length=64, unique=True)
    # League this season is for
    fkLeague = models.ForeignKey(League, on_delete=models.CASCADE)

    def edit_link(self):
        return edit_link('gametracker:season_editor', (self.pk,))

    def view_link(self):
        return view_link('gametracker:season_view', (self.pk,), self.name)

    def nav_link(self):
        return self.fkLeague.manager_link() +' | '+ self.view_link()

    def to_form_fields(self):
        return [
            {'label': 'Name: ', 'name' : 'name'    , 'value': self.name},
            {'type' : 'hidden', 'name' : 'seasonid', 'value': self.id},
            {'type' : 'hidden', 'name' : 'leagueid', 'value': self.fkLeague.id}
        ]


# Match in season involving team
class Match(models.Model):
    # Sequential round number
    round    = models.IntegerField()
    # Season of match
    fkSeason = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Date of match, optional
    date = models.DateField(null=True)

    def edit_link(self):
        return edit_link('gametracker:match_editor', (self.pk,))

    def view_link(self):
        return view_link(
            'gametracker:match_view', (self.pk,), 
            self.date.strftime('%Y_%m_%d') +'#'+ str(self.round)
        )

    def to_form_fields(self):
        return [
            {'label': 'Round #', 'name': 'round'   , 'value': self.round},
            {'label': 'Date: ' , 'name': 'date'    , 'value': self.date.date()},
            {'type' : 'hidden' , 'name': 'seasonid', 'value': self.fkSeason.id}
        ]


# Participation and score of a team in a match
class Participation(models.Model):
    # Score of team, or null if not played [yet]
    score   = models.IntegerField(null=True)
    # Match team played in, or will play in
    fkMatch = models.ForeignKey(Match, on_delete=models.CASCADE)
    # Team involved in match
    fkTeam  = models.ForeignKey(Team, on_delete=models.CASCADE)
