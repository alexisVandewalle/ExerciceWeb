from django.shortcuts import render
from disks.models import *
from .forms import *

# Create your views here.

def home(request):
    form = ResearchForm(request.POST or None)
    albums = Album.objects.all()
    if form.is_valid():
        albums = Album.objects.filter(Title__contains=form.cleaned_data['Rechercher'])
    return render(request,'disks/home.html',locals())

def voir_album(request, id):
    album = Album.objects.get(id = id)
    tracks = Track.objects.filter(album = album)
    artist = Artist.objects.get(album = album)
    return render(request,'disks/voir_album.html', locals())

def add_album(request):
    form_album = AlbumForm(request.POST or None)
    if form_album.is_valid():
        form_album.save()

    return render(request,'disks/add_album.html',locals())
