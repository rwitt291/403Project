from django.shortcuts import render
from django.http import HttpResponse
from QuickClick.models import Attempt
#import form
from .forms import ScoreForm
# Create your views here.

# Home page which will welcome the user

def indexPageView(request) :
    return render(request, 'QuickClick/index.html')

#This page will display the game where the user will be able to click and play the game!
def gamePageView(request) :#playerName) :
    if request.method == 'POST':
        newPlayer = Attempt()

        playerName = request.POST['ABBREV']
        playerScore = request.POST['score']

        newPlayer.name = playerName
        newPlayer.score = playerScore

        newPlayer.save()

        # Change this to whatever url you want after user clicks submit
        return hiScorePageView(request)

    else:
        form = ScoreForm()

    # This line is not being used
    #getPlayer = Attempt.objects.filter(name = playerName.upper())

    context = {
        #"playerNameDict" : getPlayer,
        "form" : form
    }

    return render(request, 'QuickClick/game.html', context)

# This page will display the high scores kind of like an arcade. 
# The high score will be updated and the user will be able to delete and update user
def hiScorePageView(request) :
    sQuery = Attempt.objects.all().order_by('-score')

    scoreList = sQuery

    context = {
        'scores' : scoreList
    }

    return render(request, 'QuickClick/hiscores.html', context)

def addPlayerPageView(request):
    # This currently doesn't do anything
    # We add the player within gamepageview function
    return indexPageView(request)


def editPlayerPageView(request, playerID):
    modifiedPlayerID = str(playerID)

    sQuery = "SELECT id, name, score FROM quickclick_attempt WHERE id = '" + modifiedPlayerID + "'"

    updatePerson = Attempt.objects.get(id=playerID)
    # getPlayer = Attempt.objects.raw(sQuery)
    context = {
        "playerInfo" : updatePerson,
    }

    return render (request, 'QuickClick/updatePlayer.html', context)

def storeUpdatePageView(request, playerID):
    if request.method == 'POST':
        updatePerson = Attempt.objects.get(id=playerID)

        updatePerson.name = request.POST['ABBREV']
        updatePerson.save()

        return hiScorePageView(request)

    else:
        return hiScorePageView(request)

def deletePlayer(request, playerID):
    deletePerson = Attempt.objects.get(id=playerID)

    deletePerson.delete()

    return hiScorePageView(request)