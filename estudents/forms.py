from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from estudents.models import *


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['naran', 'sexo', 'hela_fatin', 'data_moris', 'no_telefone','municipio','foto','bio']
        widgets = {
            'data_moris' : forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(EstudanteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('naran', css_class='form-group col-md-4 mb-0'),
                Column('sexo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('hela_fatin', css_class='form-group col-md-4 mb-0'),
                Column('data_moris', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('no_telefone', css_class='form-group col-md-4 mb-0'),
                Column('municipio', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('foto', css_class='form-group col-md-4 mb-0'),
                Column('bio', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save Student', css_class='btn btn-primary')
        )

   
class FormKlasCourseEstudents(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Expecting a student_id to filter the queryset
        student_id = kwargs.pop('student_id', None)
        super().__init__(*args, **kwargs)
        if student_id:
            # Filter the student field to show only the recently created student
            self.fields['estudante'].queryset = Students.objects.filter(id=student_id)
    class Meta:
        model = KlaseEstudante
        fields = ['estudante','controluestudante','estado']

class FormMateria(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['naran_materia']

class FormProfessor(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['naran', 'sexo', 'hela_fatin', 'email', 'no_telefone','municipio','foto', 'bio']


    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.helper = FormHelper()
         self.helper.layout = Layout(
		     Row(
			     Column('username', css_class='form-group col-md-4 mb-0'),
			     Column('email', css_class='form-group col-md-4 mb-0'),
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