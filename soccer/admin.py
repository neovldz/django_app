from django.contrib import admin

from soccer.models import Team, Player, Coach

# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
