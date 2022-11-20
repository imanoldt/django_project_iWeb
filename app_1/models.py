from django.db import models
from django import forms


VIDEO_CATHEGORY = (
    ("1", "COMIDA"),
    ("2", "DEPORTE"),
    ("3", "ENTRETENIMIENTO"),
    ("4", "OCIO"),
    ("5", "SERIE"),
    ("6", "VIAJES"),
    ("7", "BUSINESS"),
)
USER_AUTH = 'auth.User'


class Channel(models.Model):
    channel_name = models.CharField(
        max_length=50, blank=False, null=False, default='')
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.OneToOneField(
        USER_AUTH, on_delete=models.CASCADE, blank=False, null=True, default='')


class Video(models.Model):  # MODIFICADO
    title = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True)
    # MINIATURA DE IMAGEN PARA MEJOR OPTIMIZACION DE LA PAGINA
    thumnail = models.CharField(max_length=2000, null=True)
    # DURACION DEL VIDEO ENTERO
    length = models.IntegerField(null=True, default=0)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    likes = models.IntegerField(null=True, default=0)
    cathegory = models.CharField(
        max_length=300, null=True, choices=VIDEO_CATHEGORY, default='')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                blank=True, null=True, default='', related_name='videos')

    def __str__(self):  # DEVUELVE STRING DE LO QUE QUEREMOS VISUALIZAR / TOSTRING() _ JAVA
        return self.title


class Comment(models.Model):  # MODIFICADO
    title = models.TextField(max_length=300, default='')
    dateTime = models.DateTimeField(auto_now=True, blank=False, null=False)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, blank=False, null=True, default='', related_name='comentarios')
