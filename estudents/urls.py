
from django.urls import path
from estudents.views import *

urlpatterns = [ 


    

    # url for students
    # dadus estudante geral
    path('lista-estudante/', ListaEstudante, name="lista-estudante"),
    path('lista-estudante/aumenta', ListaAumentaEstudante, name="estudante-aumenta"),
    path('lista-estudante/hadia/<str:id>', ListaHadiaEstudante, name="estudante-hadia"),
    path('lista-estudante/delete/<str:id>', ListaDeleteEstudante, name="delete-estudante"),

    # dadus estudante baseia ao curso
    path('dadus-estudante/<str:id>', DadusEstudante, name="dadus-estudante"),

    # detail dadus klase estudante
    path('dadus-klase/estudante/<str:id>', DadusEstudanteKlase, name="detail-klase-estudante"),

   

    #url for Teacher


    path('lista-Kurso', ListaKurso, name="lista-kurso"),
    path('lista-Kurso/aumenta', AumentaListaKurso, name="aumenta-kurso"),
    path('lista-Kurso/hadia/<str:id>', HadiaListaKurso, name="hadia-kurso"),
    path('lista-Kurso/delete/<str:id>', DeleteListaKurso, name="delete-kurso"),


    path('estudante/kurso/<str:id>', DadusEstudanteKurso, name="dadus-estudante-kurso"),    
    path('estudante/kurso/<str:kurso_id>/klase/<str:klase_id>', DadusEstudanteKlase, name="detail-estudante-klase"),

    path('profile/estudante/<str:id>', DetailEstudante, name="profile-estudante"),


    path('profile/noscar/', NoscarDetail, name="noscar-profile-detail"),
    
    path('redirect/', login_redirect_view, name='login_redirect'),

    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),


    path('student/dashboard/', student_dashboard, name='student_dashboard'),    

    path('no-permission/', no_permission, name='no_permission'),
]