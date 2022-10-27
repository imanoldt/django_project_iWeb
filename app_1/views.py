from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

PUBLIC_DOMAIN_NAME = '127.0.0.1:8000'
# Create your views here.
def login(request):
    return render(request, "Login-Bootstrap-5/index.html")


def sign_up(request):
    return render(request, "Login-Bootstrap-5/sign_up.html")
