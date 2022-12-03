from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm
from .models import UploadVideo
from django.forms import ModelForm

#Formulario de registro con login 
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)

#Formulario de registro con Sign_UP 
class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', max_length=20)

#Formulario de registro con Sign_UP 
class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
#Formulario de registro Video
class NewVideoForm(forms.ModelForm):
    ## especificcar que use el modelo UploadVideo ya creado
    class Meta:
        model=UploadVideo
        ##fields=['title','description','file']
        fields='__all__'
        
    