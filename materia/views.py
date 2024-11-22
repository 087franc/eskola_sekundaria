from django.shortcuts import render,redirect
from estudents.forms import *
from estudents.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import UserEstudante

from user.decorators import allowed_users
# Create your views here.
# views for subjects 
@login_required
def ListaMateria(request):
    dadus = Subjects.objects.all()
    # dadus = Subjects.objects.prefetch_related('materia').all()
    context = {
        'title': "Lista Materia Sira",
        'dadus': dadus,
    }
    return render(request, 'materia/lista-materia.html',context)

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
    return render(request, 'materia/formulario-materia.html',context)

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
    return render(request, 'materia/formulario-materia.html',context)

@login_required
def ListaMateriaDelete(request,id):
    data = Subjects.objects.get(id=id)
    data.delete()
    messages.success(request, f'Dadus {data.naran_materia} Hamos ho Susesu')
    return redirect('lista-materia')

# dadus estudante
@login_required
@allowed_users(allowed_roles=['students'])
def DadusMateria(request):
    user = UserEstudante.objects.get(user=request.user)

    klasseEstudante = KlaseEstudante.objects.filter(estudante=user.estudante)
    klasseAtivu = KlaseEstudante.objects.filter(estudante=user.estudante,estado="ativu").last()
    print("klasseEstudante:",klasseEstudante)
    print("klasseAtivu:",klasseAtivu)
    materiaKlasseAtivu = KontroluMateria.objects.filter(controlukursuklase=klasseAtivu.controluestudante)
    print("materiaKlasseAtivu:",materiaKlasseAtivu)
    print("user:",user)

    context = {
        'title': f"Dadus Materia - {user.estudante.naran}",
        'klasseEstudante': klasseEstudante,
        'materiaKlasseAtivu': materiaKlasseAtivu,
        # 'button': "Hadia"
    }
    return render(request, 'estudante/dadus-materia.html',context)