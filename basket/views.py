from django.shortcuts import render
from basket.models import Player, Coach
from basket.forms import PlayerForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.db.models import Q


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'Core/index.html'
    return render(request, template_name, data)


def coachList(request):
    if request.method == 'POST':
        if request.POST['search[value]'] == '':
            query = Coach.objects.all()[int(request.POST['start']):int(request.POST['start']) + int(request.POST['length'])]
            json = {"recordsTotal": Coach.objects.all().count(),
                    "recordsFiltered": Coach.objects.all().count()}
        else:
            query = Coach.objects.filter(Q(name__icontains=request.POST['search[value]']) | Q(age__icontains=request.POST['search[value]']) | Q(email__icontains=request.POST['search[value]']) | Q(nickname__icontains=request.POST['search[value]']) | Q(rut__icontains=request.POST['search[value]']) | Q(dv__icontains=request.POST['search[value]']))
            json = {"recordsTotal": query.count(),
                    "recordsFiltered": query.count()}
        data = []
        for x in query:
            data.append({'rut': str(x.rut) + '-' + str(x.dv),
                         'name': x.name,
                         'nickname': x.nickname,
                         'age': x.age,
                         'email': x.email})
        json['data'] = data
        return JsonResponse(json)
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
