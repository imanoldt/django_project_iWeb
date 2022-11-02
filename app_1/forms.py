from django import forms
from django.utils.safestring import mark_safe

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
class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()


