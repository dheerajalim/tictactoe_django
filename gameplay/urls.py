# from django.conf.urls import url
from django.urls import path
from .views import game_detail, make_move, AllGameList
urlpatterns = [

    path('detail/<int:id>', game_detail, name='gameplay_detail'),
    path('make_move/<int:id>', make_move, name='gameplay_make_move'),
    path('all', AllGameList.as_view()),
]
