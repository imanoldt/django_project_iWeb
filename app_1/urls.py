from django.urls import path
from . import views
#from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('base/', views.base_main, name='base'),
    path('base2/profile/', views.profile, name='profile'),
    path('base/player/', views.player, name='player'),
   # path('padre/', views.padre2, name='padre2'),
]
