from django.contrib import admin
from .models import Invitation

# Register your models here.


@admin.register(Invitation)
class InvitationDisplay(admin.ModelAdmin):
    list_display = ['id','from_user', 'to_user', 'message', 'timestamp']
