from django import forms
from django.db.models.fields import IntegerField
from django.forms.widgets import TextInput

class ScoreForm(forms.Form) :
    score = forms.IntegerField(initial=0, label="score", widget=forms.HiddenInput())

class IndexForm(forms.Form) :
    playerName = forms.CharField(widget=TextInput(), label="playerName")