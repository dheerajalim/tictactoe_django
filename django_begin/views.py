from django.http import HttpResponse
from django.shortcuts import render , redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'django_begin/welcome.html')
