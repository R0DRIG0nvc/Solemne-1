from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse
from basket.function import *


def index(request):
    data = {}

    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = '../Template/Basket/index.html'
    return render(request, template_name, data)


def addPlayer(request):
    data = {}
    if request.method == "POST":
            data['form'] = PlayerForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_playerList')

    else:
        data['form'] = PlayerForm()

        template_name = "../Template/Basket/Add/addPlayer.html"
        return render(request, template_name, data)


def addTeam(request):
    data = {}
    if request.method == "POST":
            data['form'] = TeamForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_teamList')

    else:
        data['form'] = TeamForm()

        template_name = "../Template/Basket/Add/addTeam.html"
        return render(request, template_name, data)


def addCoach(request):
    data = {}
    if request.method == "POST":
            data['form'] = CoachForm(request.POST, request.FILES)
            data['user'] = UserForm(request.POST)

            if data['form'].is_valid() and data['user'].is_valid():
                user = data['user'].save()
                coach = data['form'].save(commit=False)
                coach.user = user
                coach.save()

                return redirect('basket_coachList')

    else:
        data['form'] = CoachForm()
        data['user'] = UserForm()

        template_name = "../Template/Basket/Add/addCoach.html"
        return render(request, template_name, data)


def addMatch(request):
    data = {}
    if request.method == "POST":
            data['form'] = MatchForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_matchList')

    else:
        data['form'] = MatchForm()

        template_name = "../Template/Basket/Add/addMatch.html"
        return render(request, template_name, data)


def addMatchRoster(request):
    data = {}
    if request.method == "POST":
            data['form'] = MatchRosterForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_index')

    else:
        data['form'] = MatchRosterForm()

        template_name = "../Template/Basket/Add/addMatchRoster.html"
        return render(request, template_name, data)


def addRoster(request):
    data = {}
    if request.method == "POST":
            data['form'] = RosterForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_rosterList')

    else:
        data['form'] = RosterForm()

        template_name = "../Template/Basket/Add/addRoster.html"
        return render(request, template_name, data)


def addRosterSelection(request):
    data = {}
    if request.method == "POST":
            data['form'] = RosterSelectionForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_rosterSelectionList')

    else:
        data['form'] = RosterSelectionForm()

        template_name = "../Template/Basket/Add/addRosterSelection.html"
        return render(request, template_name, data)


def editPlayer(request, player_id):
    data = {}
    if request.POST:
        formPlayer = EditPlayerForm(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('basket_playerList')
    template_name = '../Template/Basket/Edit/editPlayer.html'
    data['player'] = EditPlayerForm(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)


def editCoach(request, coach_id):
    data = {}
    if request.POST:
        formCoach = EditCoachForm(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formCoach.is_valid():
            formCoach.save()
            return redirect('basket_coachList')
    template_name = '../Template/Basket/Edit/editCoach.html'
    data['coach'] = EditCoachForm(instance=Coach.objects.get(pk=coach_id))

    return render(request, template_name, data)


def editTeam(request, team_id):
    data = {}
    if request.POST:
        formTeam = EditTeamForm(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formTeam.is_valid():
            formTeam.save()
            return redirect('basket_teamList')
    template_name = '../Template/Basket/Edit/editTeam.html'
    data['team'] = EditTeamForm(instance=Team.objects.get(pk=team_id))

    return render(request, template_name, data)


def coachList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, Coach)
            for x in query:
                data.append({'rut': str(x.rut) + '-' + str(x.dv),
                             'name': x.name,
                             'nickname': x.nickname,
                             'age': x.age,
                             'email': x.email,
                             'action': '<div class="btn-group" data-pk="' + str(x.pk) + '"> \
                                          <button type="button" class="btn btn-primary  btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="true">Acciones \
                                            <span class="caret ml5"></span> \
                                          </button> \
                                          <ul class="dropdown-menu" role="menu"> \
                                            <li style="cursor:pointer" class="edit"> \
                                              <a href=' + reverse('basket_editCoach', kwargs={'coach_id': x.pk}) + '>Editar</a> \
                                            </li> \
                                            <li class="divider"></li> \
                                            <li style="cursor:pointer" class="delete"> \
                                              <a>Eliminar</a> \
                                            </li> \
                                          </ul> \
                                        </div>'})
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            Coach.objects.get(pk=request.POST['coach_pk']).delete()
            return JsonResponse({})
    template_name = 'Basket/List/coachList.html'
    return render(request, template_name, {})


def playerList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, Player)
            for x in query:
                data.append({'logo': '<img src="' + x.picture.url + '" alt="Foto" class="img-thumbnail" style="with: 50px; height: 50px">',
                             'rut': str(x.rut) + '-' + str(x.dv),
                             'name': x.name,
                             'nickname': x.nickname,
                             'team': x.team.name,
                             'position': x.position,
                             'age': x.age,
                             'email': x.email,
                             'action': '<div class="btn-group" data-pk="' + str(x.pk) + '"> \
                                          <button type="button" class="btn btn-primary  btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="true">Acciones \
                                            <span class="caret ml5"></span> \
                                          </button> \
                                          <ul class="dropdown-menu" role="menu"> \
                                            <li style="cursor:pointer" class="edit"> \
                                              <a href=' + reverse('basket_editPlayer', kwargs={'player_id': x.pk}) + '>Editar</a> \
                                            </li> \
                                            <li class="divider"></li> \
                                            <li style="cursor:pointer" class="delete"> \
                                              <a>Eliminar</a> \
                                            </li> \
                                          </ul> \
                                        </div>'})
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            Player.objects.get(pk=request.POST['player_pk']).delete()
            return JsonResponse({})
    template_name = 'Basket/List/playerList.html'
    return render(request, template_name, {})


def teamList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, Team)
            for x in query:
                data.append({'logo': '<img src="' + x.logo.url + '" alt="Foto" class="img-thumbnail" style="with: 50px; height: 50px">',
                             'name': x.name,
                             'description': x.description,
                             'coach': x.coach.name,
                             'action': '<div class="btn-group" data-pk="' + str(x.pk) + '"> \
                                          <button type="button" class="btn btn-primary  btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="true">Acciones \
                                            <span class="caret ml5"></span> \
                                          </button> \
                                          <ul class="dropdown-menu" role="menu"> \
                                            <li style="cursor:pointer" class="edit"> \
                                              <a href="' + reverse('basket_editTeam', kwargs={'team_id': x.pk}) + '">Editar</a> \
                                            </li> \
                                            <li class="divider"></li> \
                                            <li style="cursor:pointer" class="delete"> \
                                              <a>Eliminar</a> \
                                            </li> \
                                          </ul> \
                                        </div>'})
            json['data'] = data
            return JsonResponse(json)
        elif request.POST['action'] == 'delete':
            Team.objects.get(pk=request.POST['team_pk']).delete()
            return JsonResponse({})
    template_name = 'Basket/List/teamList.html'
    return render(request, template_name, {})


def matchList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, Match)
            for x in query:
                data.append({'team': '<img src="' + x.local.logo.url + '" alt="Foto" style="with: 25px; height: 25px"> <b>' + x.local.name + '</b> v/s <b>' + x.visit.name + '</b> <img src="' + x.visit.logo.url + '" alt="Foto" style="with: 25px; height: 25px"> ',
                             'date': x.date})
            json['data'] = data
            return JsonResponse(json)
    template_name = 'Basket/List/matchList.html'
    return render(request, template_name, {})


def rosterList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, Roster)
            for x in query:
                data.append({'name': x.name})
            json['data'] = data
            return JsonResponse(json)
    template_name = 'Basket/List/rosterList.html'
    return render(request, template_name, {})


def rosterSelectionList(request):
    if request.method == 'POST':
        if request.POST['action'] == 'datatable':
            data = []
            query, json = paginationDataTable(request.POST, RosterSelection)
            for x in query:
                data.append({'name': x.roster.name,
                             'player': x.player.name})
            json['data'] = data
            return JsonResponse(json)
    template_name = 'Basket/List/rosterSelectionList.html'
    return render(request, template_name, {})
