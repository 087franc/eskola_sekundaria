# from pyexpat.errors import messages

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

# def DadusListaEstudante(request):
#     lista_mun_data = Students.objects.values('municipio').annotate(total=Count('municipio'))
#     lista_mun = [item['municipio'] for item in lista_mun_data]
#     numeru_mun = [item['total'] for item in lista_mun_data]

#     lista_sexo_data = Students.objects.values('sexo').annotate(total=Count('sexo'))
#     lista_sexo = [item['sexo'] for item in lista_sexo_data]
#     numeru_sexo = [item['total'] for item in lista_sexo_data]   

#     context = {      
#         'lista_mun': lista_mun,
#         'numeru_mun': numeru_mun,
#         'lista_sexo': lista_sexo,
#         'numeru_sexo': numeru_sexo
#     }
#     return render(request, 'administrador/index.html',context)    

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
    data = Students.objects.get(id=id)
    context = {
        'dadus' : data,
        'title' : f"Detail Estudante {data.naran} nia Identidade",        
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



# dadus Klasse
@login_required
def ListaKlase(request):
    data = Klasse.objects.all()
    context = {
        'title' : "Lista Klasse",
        'dadus' : data
    }
    return render(request, 'administrador/klase/klase.html',context)

@login_required
def AumentaListaKlase(request):
    if request.method == "POST":
        form = FormKlasse(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dadus Klasse Aumenta ho Susesu!")
            return redirect('lista-klasse')
    else:
        form = FormKlasse() 
    context = {
        'title' : "Aumenta Lista Klasse",
        'form' : form,
        'page' : "Klasse",
        'button' : "Aumenta",
    }
    return render(request, 'administrador/klase/formulario-klase.html',context)

@login_required
def HadiaListaKlase(request,id):
    data = Klasse.objects.get(id=id)
    if request.method == "POST":
        form = FormKlasse(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dadus {data.naran_klase} Hadia ho Susesu!")
            return redirect('lista-klasse')
    else:
        form = FormKlasse(instance=data)
    context = {
        'title' : "Formulario Hadia Dadus Klase",
        'button': "Hadia",
        'form' : form,
    }
    return render(request, 'administrador/klase/formulario-klase.html',context)

@login_required
def DeleteListaKlase(request,id):
    data = Klasse.objects.get(id=id)
    data.delete()
    messages.success(request, f"Dadus {data.naran_klase} Hamos ho Susesu!")
    return redirect('lista-klasse')

# @login_required
# def DetailStudents(request):
   
#     return render(request, 'administrador/index.html',context)