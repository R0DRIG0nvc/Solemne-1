from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.http import JsonResponse


def index(request):
    data = {}

    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = '../Template/Core/index.html'
    return render(request, template_name, data)


def addPlayer(request):
    data = {}
    if request.method == "POST":
            data['form'] = PlayerForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('player')

    else:
        data['form'] = PlayerForm()

        template_name = "../Template/Core/addPlayer.html"
        return render(request, template_name, data)


def addTeam(request):
    data = {}
    if request.method == "POST":
            data['form'] = TeamForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('player')

    else:
        data['form'] = TeamForm()

        template_name = "../Template/Core/addTeam.html"
        return render(request, template_name, data)


def addCoach(request):
    data = {}
    if request.method == "POST":
            data['form'] = CoachForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('player')

    else:
        data['form'] = CoachForm()

        template_name = "../Template/Core/addCoach.html"
        return render(request, template_name, data)


def editPlayer(request, player_id):
    data = {}
    if request.POST:
        formPlayer = EditPlayerForm(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('player')
    template_name = '../Template/Core/editPlayer.html'
    data['player'] = EditPlayerForm(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)


def editCoach(request, coach_id):
    data = {}
    if request.POST:
        formCoach = EditCoachForm(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formCoach.is_valid():
            formCoach.save()
            return redirect('player')
    template_name = '../Template/core/editCoach.html'
    data['coach'] = EditCoachForm(instance=Coach.objects.get(pk=coach_id))

    return render(request, template_name, data)


def editTeam(request, team_id):
    data = {}
    if request.POST:
        formTeam = EditTeamForm(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formTeam.is_valid():
            formTeam.save()
            return redirect('player')
    template_name = '../Template/core/editTeam.html'
    data['team'] = EditTeamForm(instance=Team.objects.get(pk=team_id))

    return render(request, template_name, data)
