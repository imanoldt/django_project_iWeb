from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10)
    edad = models.IntegerField()
    contrasenya = forms.CharField(widget=forms.PasswordInput)

