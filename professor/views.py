import os
from django.shortcuts import get_object_or_404, render,redirect

from estudents.decorators import group_required
from estudents.forms import *
from estudents.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.models import Profile
# Create your views here.
# view for Teacher
@login_required
def ListaProfessor(request):
    data = Teacher.objects.all()
    context = {
        'title' : "Lista Professor",
        'dadus' : data,
    }
    return render(request, 'professor/lista-professor.html',context)

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
    return render(request, 'professor/formulario-professor.html',context)

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
    return render(request, 'professor/formulario-professor.html',context)

@login_required
def ListaProfessorHamos(request,id):
    dadus = Teacher.objects.get(id=id)
    if dadus.foto and os.path.isfile(dadus.foto.path):
        os.remove(dadus.foto.path)
    dadus.delete()
    messages.success(request, f'Dadus {dadus.naran} Hamos ho Susesu!')
    return redirect('lista-professor')


@login_required
def DetailProfessor(request,id):
    professor = Teacher.objects.get(id=id)
    materia = KontrolaProfessorMateria.objects.filter(professor=professor)    
    bio = professor.bio.splitlines()
    context = {
        'title' : f"Professor {professor.naran} nia identidade",
        'professor':professor,
        'dadus':materia,
        'lines':bio,
    }
    print("professor", professor)
    print("materia", materia)
   
    return render(request, 'professor/detail-professor.html',context)


@group_required('teachers')
def teacher_dashboard(request):    
    profile = get_object_or_404(Profile, user=request.user)

    context = {        
        'profile' : profile,
    }
    return render(request, 'professor/teacher_index.html',context)