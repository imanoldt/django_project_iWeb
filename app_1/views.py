from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as login_process
from django.contrib.auth import authenticate


# importar modelo video
from app_1.models import Video

PUBLIC_DOMAIN_NAME = '127.0.0.1:8000'


class login(View):
    def get(self, request):
        form = AuthenticationForm()
        print(form)
        return render(request, "Login-Bootstrap-5/index.html", {"form": form})

    def post(self, request):
        print(request.POST)
        form = AuthenticationForm(data = request.POST)  ###aqui daba el fallo 
        print(form.errors.as_data)
        print(form.is_bound)
        if form.is_valid():  ## porque NO era valido :)
            nom_usu = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usu = authenticate(username=nom_usu, password=password)  ## y aqui tambn 
            if usu is not None:
                login_process(request, usu)
                return redirect('videos')
                ##return HttpResponse('hola') ##le pasas al redirect que tenias antes
            else:
                return HttpResponse('no funciono 1 ')
        else:
            return HttpResponse('no funciono 2')


class sign_upView(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "Login-Bootstrap-5/sign_up.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usu = form.save()
            login_process(
                request, usu, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect('/base/videos')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, "Login-Bootstrap-5/sign_up.html", {"form": form})


class VideoListView (ListView):
    model = Video
    template_name = 'app_1/videos.html'


class ProfileListView (ListView):
    model = Video
    template_name = 'app_1/profile.html'

class base (DetailView):
    template_name = 'app_1/base.html'

class base (DetailView):
    template_name = 'app_1/base2.html'

def upload(request):
    return render(request, 'app_1/upload.html')

def player(request, titulo):

    video = Video.objects.get(title=titulo)
    context = {
        'video': video,
    }
    return render(request, 'app_1/player.html', context)


def stadistics(request):
    video = Video.objects.all()
    return render(request, 'app_1/stadistics.html', {"videos": video})
