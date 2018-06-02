from django.forms import ModelForm
from basket.models import *
from django import forms
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
        }
        fields = ['username', 'password']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        exclude = []


class TeamForm(ModelForm):
    class Meta:
        model = Team
        exclude = []


class CoachForm(ModelForm):
    class Meta:
        model = Coach
        exclude = ['user']


class EditPlayerForm(ModelForm):
    def init(self, args, **kwargs):
        super(EditPlayerForm, self).init(args, **kwargs)
        self.fields['picture'].required = False

    class Meta:
        model = Player
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'dv': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'height': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
        }
        exclude = []


class EditCoachForm(ModelForm):
    class Meta:
        model = Coach
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'dv': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }
        exclude = ['user']


class EditTeamForm(ModelForm):
    class Meta:
        model = Team
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}),
        }
        exclude = []


class MatchForm(ModelForm):
    class Meta:
        model = Match
        exclude = []


class RosterForm(ModelForm):
    class Meta:
        model = Roster
        exclude = ['team']


class RosterSelectionForm(ModelForm):
    class Meta:
        model = RosterSelection
        exclude = []


class MatchRosterForm(ModelForm):
    class Meta:
        model = MatchRoster
        exclude = []
