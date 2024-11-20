
from django.urls import path
from professor.views import *

urlpatterns = [ 

    path('lista-professor/', ListaProfessor, name="lista-professor"),
    path('lista-professor/aumenta', ListaProfessorAuementa, name="lista-professor-aumenta"),
    path('lista-professor/hadia/<str:id>', ListaProfessorHadia, name="lista-professor-hadia"),
    path('lista-professor/delete/<str:id>', ListaProfessorHamos, name="lista-professor-hamos"),

    
    path('profile/professor/<str:id>', DetailProfessor, name="detail-professor"),
    
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    

]