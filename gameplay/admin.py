from django.contrib import admin
from .models import Move, Game


# Register your models here.
# admin.site.register(Move)
# admin.site.register(Game)

# Now in order to change the view of how it appears in admin pannel
@admin.register(Game)
class GameDisplay(admin.ModelAdmin):
    list_display = ['id', 'first_player', 'second_player', 'status', 'start_time', 'last_active'] # Displays the listed details

    list_editable = ['status'] # Makes the status field have drop down

@admin.register(Move)
class MoveDisplay(admin.ModelAdmin):
    list_display = ['id', 'x', 'y', 'comment', 'by_first_player', 'game']
