from django.db import models


# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_lenght=20)
    edad = models.IntegerField())
    contrasenya = forms.CharField(widget=forms.PasswordInput)

