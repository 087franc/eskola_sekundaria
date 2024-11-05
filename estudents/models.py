from django.db import models


class Course(models.Model):
    naran_kurso = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naran_kurso}"


class Klasse(models.Model):
    naran_klase = models.CharField(max_length=255)
    kurso = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naran_klase}"

class Teacher(models.Model):
    naran = models.CharField(max_length=255)
    sexo_choices = [
        ('Hili Sexo', 'Hili Sexo'),
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
        ('Seluk', 'Seluk'),
    ]
    sexo = models.CharField(max_length=20, choices=sexo_choices, default='Hili Sexo')
    no_telefone = models.CharField(max_length=15, null=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    hela_fatin = models.CharField(max_length=255)
    municipio_choices = [
        ('Hili Municipio', 'Hili Municipio'),
        ('Ainaro', 'Ainaro'),
        ('Aileu', 'Aileu'),
        ('Atauro', 'Atauro'),
        ('Bobonaro', 'Bobonaro'),
        ('Baucau', 'Baucau'),
        ('Dili', 'Dili'),
        ('Cova-Lima', 'Cova-Lima'),
        ('Ermera', 'Ermera'),
        ('Liquica', 'Liquica'),
        ('Lospalos', 'Lospalos'),
        ('Manatuto', 'Manatuto'),
        ('Manu-Fahi', 'Manu-Fahi'),
        ('Oecusse', 'Oecusse'),
        ('Viqueque', 'Viqueque'),
    ]
    municipio = models.CharField(max_length=20, choices=municipio_choices, default='Hili Municipio')
    foto = models.ImageField(upload_to='professor', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naran}"


class Subjects(models.Model):
    naran_materia = models.CharField(max_length=255)
    kurso = models.ForeignKey(Course, on_delete=models.CASCADE)
    professor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    klase = models.ForeignKey(Klasse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.naran_materia}"
    


class Students(models.Model):
    GENDER_CHOICES = [
        ('Hili Sexo!', 'Hili Sexo!'),
        ('Mane', 'Mane'),
        ('Feto', 'Feto'),
        ('Seluk', 'Seluk'),
    ]
    
    MUNICIPALITY_CHOICES = [
        ('Hili Municipio!', 'Hili Municipio!'),
        ('Ainaro', 'Ainaro'),
        ('Aileu', 'Aileu'),
        ('Atauro', 'Atauro'),
        ('Bobonaro', 'Bobonaro'),
        ('Baucau', 'Baucau'),
        ('Dili', 'Dili'),
        ('Cova-Lima', 'Cova-Lima'),
        ('Ermera', 'Ermera'),
        ('Liquica', 'Liquica'),
        ('Lospalos', 'Lospalos'),
        ('Manatuto', 'Manatuto'),
        ('Manu-Fahi', 'Manu-Fahi'),
        ('Viqueque', 'Viqueque'),
    ]

    naran = models.CharField(max_length=255)
    materia = models.ManyToManyField(Subjects, related_name='students') 
    data_moris = models.DateField(null=True)
    kurso = models.ForeignKey(Course, on_delete=models.CASCADE)  
    klase = models.OneToOneField(Klasse, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    sexo = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Choose Gender')
    no_telefone = models.CharField(max_length=15, null=True, unique=True)
    hela_fatin = models.CharField(max_length=255)
    municipio = models.CharField(max_length=20, choices=MUNICIPALITY_CHOICES, default='Choose Municipality')
    foto = models.ImageField(upload_to='estudante', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.naran






