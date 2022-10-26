from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"Login-Bootstrap-5/index.html")