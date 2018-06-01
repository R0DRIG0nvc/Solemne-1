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
            # 'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }
        # fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']
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
        # fields = ['name', 'age', 'email', 'nickname', 'rut', 'dv']
        exclude = []


class EditTeamForm(ModelForm):
    class Meta:
        model = Team
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'type': 'text'}),
            # 'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }
        # fields = ['name', 'logo', 'description']
        exclude = []
