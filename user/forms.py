# estudents/forms.py

# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
    
class FormBio(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Expecting a student_id to filter the queryset
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        if user_id:
            # Filter the student field to show only the recently created student
            self.fields['user'].queryset = User.objects.filter(id=user_id)
    class Meta:
        model = Profile
        fields = '__all__'
   

from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Password Tuan",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Prense password tuan'}),
    )
    new_password1 = forms.CharField(
        label="Password Foun",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password foun'}),
    )
    new_password2 = forms.CharField(
        label="Komfirma Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'komfirma password'}),
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']