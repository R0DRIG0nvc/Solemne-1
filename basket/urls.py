from django.urls import path
from basket import views


urlpatterns = [
    path('', views.index, name="basket_index"),
    path('coachList', views.coachList, name="basket_coachList"),
    path('addPlayer', views.addPlayer, name="basket_addPlayer"),
    path('addTeam', views.addTeam, name="basket_addTeam"),
    path('addCoach', views.addCoach, name="basket_addCoach"),
    path('addMatch', views.addMatch, name="basket_addMatch"),
    path('addMatchRoster', views.addMatchRoster, name="basket_addMatchRoster"),
    path('addRoster', views.addRoster, name="basket_addRoster"),
    path('addRosterSelection', views.addRosterSelection, name="basket_addRosterSelection"),
    path('editPlayer/<int:player_id>', views.editPlayer, name="basket_editPlayer"),
    path('editCoach/<int:coach_id>', views.editCoach, name="basket_editCoach"),
    path('editTeam/<int:team_id>', views.editTeam, name="basket_editTeam"),
    # path('list', views.index, name="player_list"),
    # path('add', views.add, name="player_add"),
    # path('view/<int:player_id>', views.detail, name="player_detail"),
]
