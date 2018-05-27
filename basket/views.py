from django.shortcuts import render
from basket.models import Player
from basket.forms import PlayerForm
from django.shortcuts import redirect
from django.http import JsonResponse


def index(request):
    data = {}

    # SELECT * FROM player
    data['object_list'] = Player.objects.all().order_by('-id')

    template_name = 'Core/index.html'
    return render(request, template_name, data)


def addPlayer(request):
    template_name = "../Template/Core/addPlayer.html"
    if request.POST:
        print (request.POST)
        return JsonResponse({})
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
