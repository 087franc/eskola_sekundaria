from django.urls import path
from .views import *

urlpatterns = [
    path('', Login, name="login" ),
    path('logout/', Logout, name="logout" ),

    path('users/', Usuario, name="lista-usuario"),
    path('users/aumenta', register, name="aumenta-usuario"),
    path('users/hadia/<str:id>', change_password, name="hadia-lista-usuario"),
    path('users/delete/<str:id>', DeleteUsuario, name="delete-lista-usuario"),

    path('users/profile', UserProfile, name="user-profile-detail"),
]