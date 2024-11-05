from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from estudents.models import *


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['naran', 'sexo', 'hela_fatin', 'data_moris', 'no_telefone','municipio','foto','materia','kurso']

        widgets = {
            'data_moris' : forms.DateInput(attrs={'type': 'date'}),
        }

class FormMateria(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['naran', 'sexo', 'hela_fatin', 'email', 'no_telefone','municipio','foto']


    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.layout = Layout(
		     Row(
			     Column('username', css_class='form-group col-md-6 mb-0'),
			     Column('email', css_class='form-group col-md-6 mb-0'),
			css_class='form-row'
		    ),
		    HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
		    HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
	)
         

class FormKurso(forms.ModelForm):
    class Meta : 
        model = Course
        fields = ['naran_kurso']


class FormKlasse(forms.ModelForm):
    class Meta : 
        model = Klasse
        fields = '__all__'