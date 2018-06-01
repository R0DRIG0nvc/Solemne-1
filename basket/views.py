from django.shortcuts import render
from basket.models import Player, Coach
from basket.forms import PlayerForm
from django.http import JsonResponse
from django.shortcuts import redirect
from basket.function import *


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'Core/index.html'
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
