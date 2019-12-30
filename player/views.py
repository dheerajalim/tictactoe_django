from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from .models import Invitation
from .forms import InvitationForm
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.


@login_required
def home(request):

    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    finished_games = my_games.difference(active_games)
    active_games = Game.objects.active()
    invitations = request.user.invitations_received.all()
    return render(request, 'player/home.html',{'active_games':active_games,
                                               'finished_games': finished_games,
                                               'invitations': invitations})

    ''' The below is not a good practice, as the ogic should not be in view.'''

    # game_first_player = Game.objects.filter(first_player=request.user,status='F')
    # game_second_player = Game.objects.filter(second_player=request.user,status='S')
    # all_games = list(game_first_player) + list(game_second_player)
    # return render(request, 'player/home.html', {'games': all_games})
    # # return render(request, 'player/home.html', {'games': all_games},{'ngames': Game.objects.count()})


@login_required()
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request, 'player/new_invitation.html', {'form' : form})


@login_required()
def accept_invitation(request, id):

    invitation = get_object_or_404(Invitation, pk=id)

    if not request.user == invitation.to_user:
        raise PermissionDenied

    if request.method == 'POST':
        if 'accept' in request.POST:
            game = Game.objects.create(first_player=invitation.to_user, second_player=invitation.from_user)
            invitation.delete()
            return redirect(game)
        if 'deny' in request.POST:
            invitation.delete()
            return redirect('player_home')
    else:
        return render(request,'player/accept_invitation.html',{'invitation':invitation})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "player/signup_form.html"
    success_url = reverse_lazy('player_home')