from django.urls import path
from materia.views import *

urlpatterns = [ 

     # url for subjects
    path('lista-materia/', ListaMateria, name="lista-materia"),
    path('lista-materia/aumenta', ListaMateriaAumenta, name="materia-aumenta"),
    path('lista-materia/hadia/<str:id>', ListaMateriaHadia, name="hadia-materia"),
    path('lista-materia/delete/<str:id>', ListaMateriaDelete, name="delete-materia"),

]