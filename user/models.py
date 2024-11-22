from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from estudents.models import  Students

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image=models.ImageField(upload_to='media/user/', blank=True)

    def __str__(self):
        return f"{self.user.username} profile"
    
class UserEstudante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    estudante = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.estudante}"