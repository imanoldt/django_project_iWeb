from django.db import models
from django import forms


class User(models.Model):#MODIFICADO //FALTA IMPLEMENTARLO
    name = models.CharField(max_length=10)
    #CAMPO EDAD BORRADO (DUDO QUE HAGA FALTA) //FALTA IMPLEMENTARLO
    contrasenya = forms.CharField(widget=forms.PasswordInput)

VIDEO_CATHEGORY =(
    ("1", "COMIDA"),
    ("2", "DEPORTE"),
    ("3", "ENTRETENIMIENTO"),
    ("4", "OCIO"),
    ("5", "SERIE"),
    ("6", "VIAJES"),
    ("7", "BUSINESS"),
)
class Video(models.Model): #MODIFICADO
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True)
    thumnail = models.CharField(max_length=2000, null=True) #MINIATURA DE IMAGEN PARA MEJOR OPTIMIZACION DE LA PAGINA
    length = models.IntegerField(null=True) #DURACION DEL VIDEO ENTERO
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    cathegory = models.CharField(max_length=300, null=True, choices = VIDEO_CATHEGORY)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self): #DEVUELVE STRING DE LO QUE QUEREMOS VISUALIZAR / TOSTRING() _ JAVA
        return self.title
        


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):#MODIFICADO
 title = models.CharField(max_length=50, blank=False, null=False)
