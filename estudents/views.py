# from pyexpat.errors import messages

from django.http import Http404
from user.models import Profile
from django.db.models import Count
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import AbstractUser,User,Group
# from django.contrib.auth import get_user_model



from estudents.forms import *
from estudents.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# views for login
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Ita boot Login Ho Susesu....")
            return redirect('home')
        else:
            messages.error(request, "Username ou Password La los!, Favor hare didiak!")
    context = {
            'title' : "Pagina Login"
        }
    return render(request, 'administrador/authenticate/login.html',context)




# views for dashboardd
@login_required
def Dashboard (request):
    sexo_mane = Students.objects.filter(sexo='Mane').count()
    sexo_feto = Students.objects.filter(sexo='Feto').count()
    prof_feto = Teacher.objects.filter(sexo='Feto').count()
    prof_mane = Teacher.objects.filter(sexo='Mane').count()
    total_prof = Teacher.objects.all().count()
    total_estu = Students.objects.all().count()
    profile = get_object_or_404(Profile, user=request.user)

    lista_mun_data = Students.objects.values('municipio').annotate(total=Count('municipio'))
    lista_mun = [item['municipio'] for item in lista_mun_data]
    numeru_mun = [item['total'] for item in lista_mun_data]

    lista_sexo_data = Students.objects.values('sexo').annotate(total=Count('sexo'))
    lista_sexo = [item['sexo'] for item in lista_sexo_data]
    numeru_sexo = [item['total'] for item in lista_sexo_data]   
    context = {
        'sexo_mane' : sexo_mane,
        'sexo_feto' : sexo_feto,
        'prof_feto' : prof_feto,
        'prof_mane' : prof_mane,
        'total_prof' : total_prof,
        'total_estu' : total_estu,
        'profile' : profile,
        'lista_mun': lista_mun,
        'numeru_mun': numeru_mun,
        'lista_sexo': lista_sexo,
        'numeru_sexo': numeru_sexo
    
    }    
    return render(request, 'administrador/index.html',context)

# dadus estudante
def DadusEstudante(request,id):
    klase = Course.objects.get(id=id)
    kursu = Klasse.objects.filter(naran_klase=klase)
    context = {
        'title': "Dadus Estudante Ciencias Naturais",        
        'kursu': kursu,
    }
    return render(request, 'administrador/klase/dadus-klase.html',context)

# dadus klase estudante
def DadusEstudanteKlase(request,id):
    klase = Klasse.objects.get(id=id)
    estudante = Students.objects.filter(klase=klase)
    context = {
        'title' : "Dadus Estudante Kada Klase",
        'estudante': estudante,
    }
    return render(request, 'administrador/estudante/dadus-estudante.html',context)

@login_required
def ListaEstudante(request):
    dados_estudante = Students.objects.all()
    context = {
        'title':"Lista Estudante",
        'dadus' : dados_estudante,
    }
    return render(request, 'administrador/estudante/lista_estudante.html',context)


# User = get_user_model()  # Dynamically get the User model
# @login_required
# def user_list_view(request):
#     users = User.objects.all()  # Fetch all users
#     context = {
#         'title': "Lista Usuario",  # Title for the template
#         'dadus': users  # Pass the users to the template
#     }
#     return render(request, 'administrador/user.html', context) 

@login_required
def ListaAumentaEstudante(request):
    if request.method == 'POST':
        form = EstudanteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dadus Portfolio Aumenta ho Susesu')
            return redirect('lista-estudante')    
    else:
        form = EstudanteForm()
    context = {
        'title': "Formulario Aumenta Dadus Estudante",
        'page': "Estudante",
        'form':form,
        'button': 'Aumenta',
    }
    return render (request, 'administrador/estudante/formulario-estudante.html',context)

@login_required
def ListaHadiaEstudante (request,id):
    data = Students.objects.get(id=id)
    if request.method == "POST":
        form = EstudanteForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dadus {data.naran} Hadia ho Sesesu!")
            return redirect('lista-estudante')
    else:
        form = EstudanteForm(instance=data)
    context = {
        'title': "Formulario Atualiza Dadus Estudante",
        'page': "Estudante",
        'form': form,
        'button': 'Hadia',
    }
    return render(request, 'administrador/estudante/formulario-estudante.html',context)

@login_required
def ListaDeleteEstudante(request,id):
    delete_id = Students.objects.get(id=id)
    if delete_id.foto and os.path.isfile(delete_id.foto.path):
        os.remove(delete_id.foto.path)
    delete_id.delete()
    messages.success(request, f"Dadus {delete_id.naran} Hamos ho Susesu ona!")
    return redirect ('lista-estudante')


# views for subjects 
@login_required
def ListaMateria(request):
    dadus = Subjects.objects.all()
    # dadus = Subjects.objects.prefetch_related('materia').all()
    context = {
        'title': "Lista Materia Sira",
        'dadus': dadus,
    }
    return render(request, 'administrador/materia/lista-materia.html',context)

@login_required
def ListaMateriaAumenta(request):
    if request.method == 'POST':
        form = FormMateria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dadus Materia Aumenta ho Susesu!')
            return redirect('lista-materia')
    else:
        form = FormMateria()
    context = {
        'title' : "Formulario Aumenta dadus Materia",
        'page' : "Materia",
        'form' : form,
        'button': 'Aumenta'
    }
    return render(request, 'administrador/materia/formulario-materia.html',context)

@login_required
def ListaMateriaHadia(request, id):
    data = Subjects.objects.get(id=id)
    if request.method == "POST":
        form = FormMateria(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dadus {data.naran_materia} Hadia Ho Susesu!')
            return redirect('lista-materia')
    else:
        form = FormMateria(instance=data)
    context = {
        'title': "Formulario Atualiza Dadus Materia",
        'page': "Materia",
        'form': form,
        'button': "Hadia"
    }
    return render(request, 'administrador/materia/formulario-materia.html',context)

@login_required
def ListaMateriaDelete(request,id):
    data = Subjects.objects.get(id=id)
    data.delete()
    messages.success(request, f'Dadus {data.naran_materia} Hamos ho Susesu')
    return redirect('lista-materia')


# view for Teacher
@login_required
def ListaProfessor(request):
    data = Teacher.objects.all()
    context = {
        'title' : "Lista Professor",
        'dadus' : data,
    }
    return render(request, 'administrador/professor/lista-professor.html',context)

@login_required
def ListaProfessorAuementa(request):
    if request.method == "POST" :
        form = FormProfessor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dadus Professor Aumenta ho Susesu!')
            return redirect('lista-professor')
    else:
        form = FormProfessor()
    context = {
        'title': "Formulario Aumenta Dadus Professor",
        'button' : "Aumenta",
        'page' : "Professor",
        'form':form
    }
    return render(request, 'administrador/professor/formulario-professor.html',context)

@login_required
def ListaProfessorHadia(request,id):
    data = Teacher.objects.get(id=id)
    if request.method == "POST" :
        form = FormProfessor(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dadus { data.naran } Hadia Ho Susesu!')
            return redirect('lista-professor')
    else:
        form = FormProfessor(instance=data)
    context = {
        'title' : "Formulario Atualiza Dadus Professor",
        'page' : "Professor",
        'button' : "Hadia",
        'form' : form,
    }
    return render(request, 'administrador/professor/formulario-professor.html',context)

@login_required
def ListaProfessorHamos(request,id):
    dadus = Teacher.objects.get(id=id)
    if dadus.foto and os.path.isfile(dadus.foto.path):
        os.remove(dadus.foto.path)
    dadus.delete()
    messages.success(request, f'Dadus {dadus.naran} Hamos ho Susesu!')
    return redirect('lista-professor')


# Detail Estudante

def DetailEstudante(request, id):
    # Retrieve student by ID
    student = get_object_or_404(Students, id=id)
    Bio = Profile.objects.all()
    # Fetch the student's active class and course (if any)
    try:
        klase_estudante = KlaseEstudante.objects.get(estudante=student)
        course = klase_estudante.controluestudante.kurso
        klasse = klase_estudante.controluestudante.klase
    except KlaseEstudante.DoesNotExist:
        course = None
        klasse = None

    # Retrieve subjects for the student's course and class
    if course and klasse:
        subjects = KontroluMateria.objects.filter(
            controlukursuklase__kurso=course,
            controlukursuklase__klase=klasse
        )
    else:
        subjects = KontroluMateria.objects.none()

    context = {
        'student': student,
        'course': course,
        'klasse': klasse,
        'subjects': subjects,
        'title' : f"Detail Estudante {student.naran} nia Identidade",         
        'klase_estudante' : klase_estudante,              
      
    }
    print("subject", subjects)
    print("klase estudante", klase_estudante)
    print("Kourse", course)
    print("klase", klasse)
    print("student", student)
    return render(request, "administrador/estudante/detail-estudante.html",context)

    
# dadus Kurso
@login_required
def ListaKurso(request):
    data = Course.objects.all()
    context = {
        'title' : "Lista Kurso",
        'dadus' : data
    }
    return render(request, 'administrador/kurso/lista-kurso.html',context)

@login_required
def AumentaListaKurso(request):
    if request.method == "POST":
        form = FormKurso(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dadus Kurso Aumenta ho Susesu!")
            return redirect('lista-kurso')
    else:
        form = FormKurso() 
    context = {
        'title' : "Aumenta Lista Kurso",
        'form' : form,
        'page' : "Kurso",
        'button' : "Aumenta",
    }
    return render(request, 'administrador/kurso/formulario-kurso.html',context)


def HadiaListaKurso(request,id):
    data = Course.objects.get(id=id)
    if request.method == "POST":
        form = FormKurso(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dadus {data.naran_kurso} Hadia ho Susesu!")
            return redirect('lista-kurso')
    else:
        form = FormKurso(instance=data)
    context = {
        'title' : "Formulario Hadia Dadus Kurso",
        'button': "Hadia",
        'form' : form,
    }
    return render(request, 'administrador/kurso/formulario-kurso.html',context)


def DeleteListaKurso(request,id):
    data = Course.objects.get(id=id)
    data.delete()
    messages.success(request, f"Dadus {data.naran_kurso} Hamos ho Susesu!")
    return redirect('lista-kurso')

# DetailEstudanteKursu
@login_required
def DadusEstudanteKurso(request, id):
    kurso = Course.objects.get(id=id)
    klase = ControluKursuKlase.objects.filter(kurso=kurso).select_related('klase','tinan')
    context = {
        'kurso':kurso,
        'klase':klase,
    }
    return render(request, 'administrador/kurso/detail-estudante-kurso.html',context)

# DetailEstudanteKlase
@login_required
def DadusEstudanteKlase(request, kurso_id, klase_id):
    print("klase:",klase_id)
    print("kurso:",kurso_id)

    kurso = get_object_or_404(Course, id=kurso_id)    
    klase = get_object_or_404(Klasse, id=klase_id)
    print("klase:",klase)
    print("kurso:",kurso)
    students = KlaseEstudante.objects.filter(
        controluestudante__kurso=kurso,
        controluestudante__klase=klase
        ,estado='ativu'  # Optional filter for active students
    )#.select_related('estudante')
    print("students:",students)
    context = {
        'kurso':kurso,
        'klase':klase,
        'estudante':students,
    }
    
    return render(request, 'administrador/klase/detail-estudante-klase.html',context)


@login_required
def NoscarDetail(request):
    return render(request, 'administrador/eskola/about-noscar.html')

# @login_required
# def DetailStudents(request):
   
#     return render(request, 'administrador/index.html',context)