from django.db import models
from django import forms
from django.contrib.auth.models import User


VIDEO_CATHEGORY = (
    ("1", "COMIDA"),
    ("2", "DEPORTE"),
    ("3", "ENTRETENIMIENTO"),
    ("4", "OCIO"),
    ("5", "SERIE"),
    ("6", "VIAJES"),
    ("7", "BUSINESS"),
)
USER_AUTH = User


class Channel(models.Model):

    channel_name = models.CharField(
        max_length=50, blank=False, null=False, default='')
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.OneToOneField(
        USER_AUTH, on_delete=models.CASCADE, blank=False, null=True, default='')

    def __str__(self):
        return self.channel_name


class Video(models.Model):

    title = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True, blank="True")
    thumnail = models.CharField(max_length=2000, null=True, blank="True")
    length = models.IntegerField(null=True, default=0)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    likes = models.ManyToManyField(
        USER_AUTH, blank=True, related_name='post_likes')
    dislikes = models.ManyToManyField(
        USER_AUTH, blank=True, related_name='post_dislikes')
    cathegory = models.CharField(
        max_length=300, null=True, choices=VIDEO_CATHEGORY, default='')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                blank=True, null=True, default='', related_name='videos')
    file = models.FileField(upload_to="videos", blank=True, null=True)
    thumnail1 = models.ImageField(upload_to="imagenes", blank=True, null=True)

    @property
    def darlike(self):
        return self.likes.all().count()

    def __str__(self):
        return self.title

    def miniatura(self):
        if self.thumnail is None:
            #print("THUMNAIL 1: ",self.thumnail1)
            pathT=self.thumnail1.path
            #print("TRUTA ENTERA: ",pathT)
            pathT=pathT.split('app_1')
            print("NUEVO PATH: ",pathT)
            pathUltimo=pathT[1]
            pathUltimo=pathUltimo.replace('\\', '/')
            pathfinal = '../..' + pathUltimo
            print("RUTA 1: ",pathfinal)
            return pathfinal ##ruta siempre igual a caratula generica. 
        else:
            return self.thumnail

    def filename(self):  ##devuelve una string que es el path que necesito para mostrar el video. 
        try:
            pathVideo = self.file.path
            pathVideo = pathVideo.split('app_1')
            pathBueno = pathVideo[1] ##tengo la parte del path que quiero
            pathBueno = pathBueno.replace('\\', '/')
            pathfinal = '..' + pathBueno
            return pathfinal

        except:
            print('No has accedio a un video introducido por el usuario')
            return self.path  


class Comment(models.Model):

    title = models.TextField(max_length=300, default='')
    dateTime = models.DateTimeField(auto_now=True, blank=False, null=False)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, blank=False, null=True, default='', related_name='comentarios')

    def __str__(self):
        return self.title
