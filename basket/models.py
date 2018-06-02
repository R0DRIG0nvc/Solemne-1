from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES
from django.contrib.auth.models import User


class Team(models.Model):
    coach = models.OneToOneField('Coach', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm")
    weight = models.PositiveIntegerField(help_text="Peso en gramos")
    position = models.CharField(max_length=60, choices=POSITION_PLAYER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    rut = models.CharField(max_length=8)
    dv = models.CharField(max_length=1)

    picture = models.ImageField(upload_to='picture_players')

    def full_rut(self):
        return '{}-{}' . format(self.rut, self.dv)

    def __str__(self):
        return self.name


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)

    rut = models.CharField(max_length=8)
    dv = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Roster(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return '%s - %s' % (self.name, self.team.name)


class RosterSelection(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    roster = models.ForeignKey('Roster', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('roster', 'player'),)

    def __str__(self):
        return '%s - %s' % (self.roster.name, self.player.name)


class Match(models.Model):
    local = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_local')
    visit = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_visit')
    date = models.DateTimeField()

    def __str__(self):
        return '%s v/s %s' % (self.local.name, self.visit.name)


class MatchRoster(models.Model):
    match = models.OneToOneField('Match', on_delete=models.CASCADE)
    local = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='matchroster_local')
    visit = models.ForeignKey('Roster', on_delete=models.CASCADE, related_name='matchroster_visit')

    class Meta:
        unique_together = (('match', 'local', 'visit'),)

    def __str__(self):
        return '%s v/s %s - %s' % (self.local.name, self.visit.name, self.match.date)
