from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(max_length=10)
    edad = models.IntegerField()
    contrasenya = forms.CharField(widget=forms.PasswordInput)


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300, null=True)
    path = models.CharField(max_length=2000, null=True)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Channel(models.Model):
    channel_name = models.CharField(max_length=50, blank=False, null=False)
    subscribers = models.IntegerField(default=0, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
