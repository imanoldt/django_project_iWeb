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

    def __str__(self):
        return self.channel_name


class Video(models.Model):

    title = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True)
    thumnail = models.CharField(max_length=2000, null=True)
    length = models.IntegerField(null=True, default=0)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    likes = models.IntegerField(null=True, default=0)
    dislikes = models.IntegerField(null=True, default=0)
    cathegory = models.CharField(
        max_length=300, null=True, choices=VIDEO_CATHEGORY, default='')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE,
                                blank=True, null=True, default='', related_name='videos')

    def __str__(self):
        return self.title

class UploadVideo(models.Model):

    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=300, null=True)
    cathegory = models.CharField(max_length=300, null=True, choices=VIDEO_CATHEGORY, default='')
    file = models.FileField(upload_to="videos",null=True)
  

    def __str__(self):
        return self.title
        
class Comment(models.Model):

    title = models.TextField(max_length=300, default='')
    dateTime = models.DateTimeField(auto_now=True, blank=False, null=False)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, blank=False, null=True, default='', related_name='comentarios')

    def __str__(self):
        return self.title
