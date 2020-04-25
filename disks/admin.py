from django.contrib import admin
from disks.models import *

# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('Title','artist')
    search_fields = ('Title',)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)

class TrackAdmin(admin.ModelAdmin):
    list_display = ('Name','Composer','UnitPrice')
    search_fields = ('Name','Composer')

admin.site.register(Album,AlbumAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Track,TrackAdmin)