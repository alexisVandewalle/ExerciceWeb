from django import forms
from .models import *

class ResearchForm(forms.Form):
    Rechercher = forms.CharField(max_length=100)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = "__all__"