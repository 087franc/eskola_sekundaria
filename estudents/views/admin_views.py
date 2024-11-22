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



# dadus estudante
@login_required
def DadusEstudante(request,id):
    klase = Course.objects.get(id=id)
    kursu = Klasse.objects.filter(naran_klase=klase)
    context = {
        'title': "Dadus Estudante Ciencias Naturais",        
        'kursu': kursu,
    }
    return render(request, 'administrador/klase/dadus-klase.html',context)

# dadus klase estudante
@login_required
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
        if 'student_form' in request.POST:
            # Handle Student Form Submission
            student_form = EstudanteForm(request.POST, request.FILES)
            if student_form.is_valid():
                student = student_form.save()
                # Reload the form page, now showing the class and course form
                class_course_form = FormKlasCourseEstudents(student_id=student.id)
                return render(request, 'administrador/estudante/formulario-aumenta-estudante.html', {
                    'student_form': None,  # Hide the student form
                    'class_course_form': class_course_form,
                    'button': "Aumenta",
                    'title': "Formulario Aumenta Dadus Estudante",
                    'student': student,
                })
        elif 'class_course_form' in request.POST:
            # Handle Class and Course Form Submission
            class_course_form = FormKlasCourseEstudents(request.POST)
            if class_course_form.is_valid():
                # Get the student instance to associate it with the class/course assignment
                student_id = request.POST.get('student_id')
                student = Students.objects.get(id=student_id)
                assignment = class_course_form.save(commit=False)
                assignment.student = student  # Link assignment to the student
                assignment.save()
                messages.success(request, f"Dadus Estudante {student.naran} Aumenta ho Susesu")
                return redirect('lista-estudante')
    else:
        # Initial display: Only show the Student Form
        student_form = EstudanteForm()
        class_course_form = None  # Do not show the class/course form yet
    return render(request, 'administrador/estudante/formulario-aumenta-estudante.html', {
        'student_form': student_form,
        'button': "Aumenta",
        'title': "Formulario Aumenta Dadus Estudante",
    })

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
    return render(request, 'administrador/estudante/formulario-hadia-estudante.html',context)

@login_required
def ListaDeleteEstudante(request,id):
    delete_id = Students.objects.get(id=id)
    if delete_id.foto and os.path.isfile(delete_id.foto.path):
        os.remove(delete_id.foto.path)
    delete_id.delete()
    messages.success(request, f"Dadus {delete_id.naran} Hamos ho Susesu ona!")
    return redirect ('lista-estudante')



# Detail Estudante
@login_required
def DetailEstudante(request, id):
    # Retrieve student by ID
    student = get_object_or_404(Students, id=id)
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
    bio_lines = student.bio.splitlines() 
    
    context = {
        'student': student,
        'bio': bio_lines,
        'course': course,
        'klasse': klasse,
        'subjects': subjects,
        'title' : f"Detail Estudante {student.naran} nia Identidade",         
        'klase_estudante' : klase_estudante,              
      
    }
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

@login_required
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

@login_required
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

# views.py
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def login_redirect_view(request):
    if request.user.groups.filter(name='admin').exists():
        return redirect('admin_dashboard')
    elif request.user.groups.filter(name='teachers').exists():
        return redirect('teacher_dashboard')
    elif request.user.groups.filter(name='student').exists():
        return redirect('student_dashboard')
    else:
        return redirect('default_dashboard')


# views.py
from django.shortcuts import render
from user.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_dashboard(request):
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
    return render(request, 'administrador/admin_index.html',context)



@login_required
@allowed_users(allowed_roles=['students'])
def student_dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {        
        'profile' : profile,
    }
    return render(request, 'estudante/students_index.html',context)

def no_permission(request):
    return render(request, 'administrador/no_permission.html', status=403)

