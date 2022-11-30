from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import ListView, DetailView, View, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as login_process
from django.contrib.auth import login as logout_process
from django.contrib.auth import authenticate
from app_1.models import Video


PUBLIC_DOMAIN_NAME = '127.0.0.1:8000'




class error_404handle(TemplateView):
    template_name = 'error/404NotFound.html'

class error_500handle(TemplateView):
    template_name = 'error/500NotFound.html'

class login(View):

    def get(self, request):
        form = AuthenticationForm()
        print(form)
        return render(request, "Login-Bootstrap-5/index.html", {"form": form})

    def post(self, request):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            nom_usu = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usu = authenticate(
                username=nom_usu, password=password)
            if usu is not None:
                login_process(request, usu)
                return redirect('videos')
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


class LogOut(View):

    def get(self, request):
        logout_process(request)
        return redirect('login')


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
    videos_r = Video.objects.exclude(title=titulo)[:3]
    context = {
        'video': video,
        'videos_r': videos_r,
    }
    return render(request, 'app_1/player.html', context)


def stadistics(request):
    video = Video.objects.all()
    return render(request, 'app_1/stadistics.html', {"videos": video})
