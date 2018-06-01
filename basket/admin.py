from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'thumb',)

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' % (obj.logo.url))


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'nickname', 'rut', 'dv')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_rut', 'age', 'height', 'weight', 'thumb', )

    def thumb(self, obj):
        return mark_safe(u'<img src="%s" style="width:10px;height:10px;"/>' % (obj.picture.url))


@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
    pass


@admin.register(RosterSelection)
class RosterSelectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(MatchRoster)
class MatchRosterAdmin(admin.ModelAdmin):
    pass
