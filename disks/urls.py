from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name = 'home'),
    path('voir_album/<int:id>',views.voir_album, name='voir_album')
]