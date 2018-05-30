from django.forms import ModelForm
from basket.models import Player, Team, Coach
from django import forms


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']


class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv']


class EditPlayerForm(ModelForm):
    def init(self, args, **kwargs):
        super(EditPlayerForm, self).init(args, **kwargs)
        self.fields['picture'].required = False

    class Meta:
        model = Player
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': '111111111'}),
        }
        # fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
        exclude = []


class EditCoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv']


class EditTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'logo', 'description']
