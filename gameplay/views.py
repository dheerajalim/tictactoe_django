from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from django.contrib.auth.decorators import login_required
from .forms import MoveForm
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView

# Create your views here.
@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk = id)
    context = {'game' : game}
    if game.is_users_move(request.user):
        context['form'] = MoveForm()

    return render(request, 'gameplay/game_detail.html', context)


@login_required
def make_move(request, id):
    game = get_object_or_404(Game, pk=id)
    if not game.is_users_move(request.user):
        raise PermissionDenied

    move = game.new_move()
    form = MoveForm(instance=move, data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('gameplay_detail', id)
    else:
        return render(request,'gameplay/game_detail.html', {'game':game, 'form':form})


class AllGameList(ListView):
    model = Game
