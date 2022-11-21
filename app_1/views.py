from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.generic import ListView
from django.views.generic import DetailView

#importar modelo video
from app_1.models import Video

PUBLIC_DOMAIN_NAME = '127.0.0.1:8000'

# Create your views here.
def login(request):
    if "POST" == request.method:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            user_password=form.cleaned_data.get("password")
            user=authenticate(username=user_name, password=user_password)
    return render(request, "Login-Bootstrap-5/index.html")


def sign_up(request):
    return render(request, "Login-Bootstrap-5/sign_up.html")

""" @login_required
def base_main(request):
    #para importar todos los objetos videos
    video=Video.objects.all()
    #decir al render que devuelva plantilla renderizada
    return render(request, "app_1/videos.html",{"videos":video})
    #return render(request, "app_1/base.html") """




class VideoListView (ListView):
    model = Video
    template_name= 'app_1/videos.html'

class ProfileListView (ListView):
    model = Video
    template_name= 'app_1/profile.html'

""" def profile(request):
    video=Video.objects.all()
    #decir al render que devuelva plantilla renderizada
    return render(request,'app_1/profile.html',{"videos":video}) """


#MIRAR
""" def base(request):
   
   return render(request,'app_1/base.html') 
   
   def base2(request):
   
   return render(request,'app_1/base2.html')
   
   
   """

class base (DetailView):
    template_name= 'app_1/base.html'

class base (DetailView):
    template_name= 'app_1/base2.html'


     



def upload(request):
    return render(request,'app_1/upload.html')

def player(request,titulo):
    
    video = Video.objects.get(title = titulo)
    context = {
        'video' : video, 
    }
    return render(request,'app_1/player.html', context)

def stadistics(request):
    video=Video.objects.all()
    
    #context = {
    #    'video' : video, 
    #}
    return render(request,'app_1/stadistics.html',{"videos":video})
