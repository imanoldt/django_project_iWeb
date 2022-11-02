from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.template import RequestContext


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

@login_required
def base_main(request):
    return render(request, "app_1/base.html")