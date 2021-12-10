from django.urls import path 
from .views import indexPageView 
from .views import gamePageView
from .views import hiScorePageView, addPlayerPageView, editPlayerPageView, storeUpdatePageView,deletePlayer


urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('game/', gamePageView, name = 'game'),
    path('hiscores/', hiScorePageView, name = 'hiscores'),
    path('addPlayer/', addPlayerPageView, name= 'addPlayer'),
    path('editPlayer/<int:playerID>/', editPlayerPageView, name= 'editPlayer'),
    path('storeUpdate/<int:playerID>/', storeUpdatePageView, name= 'storeUpdate'),
    path('deletePlayer/<int:playerID>/', deletePlayer, name= 'deletePlayer'),
]
