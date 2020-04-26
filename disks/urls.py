from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name = 'home'),
    path('voir_album/<int:id>',views.voir_album, name='voir_album'),
    path('add_album',views.add_album, name='add_album'),
]