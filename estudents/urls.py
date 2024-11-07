
from django.urls import path
from estudents.views import *

urlpatterns = [ 


    path('login/', Login, name="login" ),
    
    path('', Dashboard, name="home"),
    # path('administrador/user', User, name="user"),

    # url for students
    path('lista-estudante/', ListaEstudante, name="lista-estudante"),
    path('lista-estudante/aumenta', ListaAumentaEstudante, name="estudante-aumenta"),
    path('lista-estudante/hadia/<str:id>', ListaHadiaEstudante, name="estudante-hadia"),
    path('lista-estudante/delete/<str:id>', ListaDeleteEstudante, name="delete-estudante"),

    # url for subjects
    path('lista-materia/', ListaMateria, name="lista-materia"),
    path('lista-materia/aumenta', ListaMateriaAumenta, name="materia-aumenta"),
    path('lista-materia/hadia/<str:id>', ListaMateriaHadia, name="hadia-materia"),
    path('lista-materia/delete/<str:id>', ListaMateriaDelete, name="delete-materia"),

    #url for Teacher

    path('lista-professor/', ListaProfessor, name="lista-professor"),
    path('lista-professor/aumenta', ListaProfessorAuementa, name="lista-professor-aumenta"),
    path('lista-professor/hadia/<str:id>', ListaProfessorHadia, name="lista-professor-hadia"),
    path('lista-professor/delete/<str:id>', ListaProfessorHamos, name="lista-professor-hamos"),

    path('lista-Kurso', ListaKurso, name="lista-kurso"),
    path('lista-Kurso/aumenta', AumentaListaKurso, name="aumenta-kurso"),
    path('lista-Kurso/hadia/<str:id>', HadiaListaKurso, name="hadia-kurso"),
    path('lista-Kurso/delete/<str:id>', DeleteListaKurso, name="delete-kurso"),

    path('lista-Klase', ListaKlase, name="lista-klasse"),
    path('lista-Klase/aumenta', AumentaListaKlase, name="aumenta-klasse"),
    path('lista-Klase/hadia<str:id>', HadiaListaKlase, name="hadia-klase"),
    path('lista-Klase/delete/<str:id>', DeleteListaKlase, name="delete-klase"),

    # path('home/chart-estudante/', DadusListaEstudante, name="chart-estudante"),

    path('profile/estudante/<str:id>', DetailEstudante, name="profile-estudante"),

    path('profile/noscar/', NoscarDetail, name="noscar-profile-detail")

    
    
]