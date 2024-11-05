
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
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
    return render(request, 'login.html',context)


@login_required
def Logout(request):
    logout(request)
    messages.success(request, "Ita boot Logout ona Husi Sistema...")
    return redirect('login')

@login_required
def Usuario(request):
    data = User.objects.prefetch_related('groups').all()
    # print("usuario",usuario)
    context = {
        'users' : data
    }
    return render(request, 'users/lista-usuario.html',context)




@login_required
def register(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to the desired page after registration
    else:
        form = CustomUserCreationForm()
    return render (request, 'users/formulario-user.html',{'form':form,'title':"Formulario Hadia Dadus Estudante", 'page':"Usuario",'button':"Aumenta"})

from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@login_required
def change_password(request,id):
    data = User.objects.get(id=id)
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('lista-usuario')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'users/formulario-user.html', {'form': form, 'title': "Formulario Hadia Password", 'page': "Usuario", 'button':"Hadia"})
 
@login_required
def DeleteUsuario(request,id):
    data = User.objects.get(id=id)
    data.delete()
    messages.success(request, "Dadus Usuario Hamos Ho Susesu!")
    return redirect('lista-usuario')

@login_required
def UserProfile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        return render(request, 'users/profile.html', {'profile': profile})
    else:
        messages.error(request, 'Ita boot nia profile seidauk kompletu!')
        return redirect('login')  