from django.shortcuts import render
from basket.models import *
from basket.forms import *
from django.shortcuts import redirect
from django.http import JsonResponse
from basket.function import *


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

                return redirect('basket_index')

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

                return redirect('basket_index')

    else:
        data['form'] = TeamForm()

        template_name = "../Template/Core/addTeam.html"
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

                return redirect('basket_index')

    else:
        data['form'] = CoachForm()
        data['user'] = UserForm()

        template_name = "../Template/Core/addCoach.html"
        return render(request, template_name, data)


def addMatch(request):
    data = {}
    if request.method == "POST":
            data['form'] = MatchForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_index')

    else:
        data['form'] = MatchForm()

        template_name = "../Template/Core/addMatch.html"
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

        template_name = "../Template/Core/addMatchRoster.html"
        return render(request, template_name, data)


def addRoster(request):
    data = {}
    if request.method == "POST":
            data['form'] = RosterForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_index')

    else:
        data['form'] = RosterForm()

        template_name = "../Template/Core/addRoster.html"
        return render(request, template_name, data)


def addRosterSelection(request):
    data = {}
    if request.method == "POST":
            data['form'] = RosterSelectionForm(request.POST, request.FILES)

            if data['form'].is_valid():
                data['form'].save()

                return redirect('basket_index')

    else:
        data['form'] = RosterSelectionForm()

        template_name = "../Template/Core/addRosterSelection.html"
        return render(request, template_name, data)


def editPlayer(request, player_id):
    data = {}
    if request.POST:
        formPlayer = EditPlayerForm(request.POST, request.FILES, instance=Player.objects.get(pk=player_id))
        if formPlayer.is_valid():
            formPlayer.save()
            return redirect('basket_index')
    template_name = '../Template/Core/editPlayer.html'
    data['player'] = EditPlayerForm(instance=Player.objects.get(pk=player_id))

    return render(request, template_name, data)


def editCoach(request, coach_id):
    data = {}
    if request.POST:
        formCoach = EditCoachForm(request.POST, request.FILES, instance=Coach.objects.get(pk=coach_id))
        if formCoach.is_valid():
            formCoach.save()
            return redirect('basket_index')
    template_name = '../Template/core/editCoach.html'
    data['coach'] = EditCoachForm(instance=Coach.objects.get(pk=coach_id))

    return render(request, template_name, data)


def editTeam(request, team_id):
    data = {}
    if request.POST:
        formTeam = EditTeamForm(request.POST, request.FILES, instance=Team.objects.get(pk=team_id))
        if formTeam.is_valid():
            formTeam.save()
            return redirect('basket_index')
    template_name = '../Template/core/editTeam.html'
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
                                              <a>Editar</a> \
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
    template_name = 'Core/coachList.html'
    return render(request, template_name, {})
# def add(request):
#     data = {}
#     if request.method == "POST":
#         data['form'] = PlayerForm(request.POST, request.FILES)
#
#         if data['form'].is_valid():
#             # aca el formulario valido
#             data['form'].save()
#
#             return redirect('player_list')
#
#     else:
#         data['form'] = PlayerForm()
#
#     template_name = 'player/add_player.html'
#     return render(request, template_name, data)
#
#
# def detail(request, player_id):
#
#     data = {}
#     template_name = 'player/detail_player.html'
#
#     # SELECT * FROM player WHERE id = player_id
#     data['player'] = Player.objects.get(pk=player_id)
#     # import pdb;pdb.set_trace()
#
#     return render(request, template_name, data)
