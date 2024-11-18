from django.urls import path
from .views import *

urlpatterns = [
    path('', Login, name="login" ),
    path('logout/', Logout, name="logout" ),

    path('users/', Usuario, name="lista-usuario"),
    path('users/aumenta/usuario', register, name="aumenta-usuario"),   
    path('users/hadia/<str:id>', change_password, name="hadia-lista-usuario"),
    path('users/delete/<str:id>', DeleteUsuario, name="delete-lista-usuario"),

     path('users/aumenta/bio', AumentaBio, name="aumenta-bio"),
     path('users/hadia/bio/<str:id>', HadiaaProfile, name="hadia-user-profile"),
     path('users/hamos/bio/<str:id>', HamosProfile, name="hamos-user-profile"),

    path('users/profile', UserProfile, name="user-profile-detail"),
]