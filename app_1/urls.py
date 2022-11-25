from django.urls import include, path
from . import views
from app_1.views import VideoListView, ProfileListView, sign_upView, login

#from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('', login.as_view(), name='login'),
    path('sign_up/', sign_upView.as_view(), name='sign_up'),
    path('base/videos', VideoListView.as_view(), name='videos'),
    path('base2/profile/', ProfileListView.as_view(), name='profile'),
    path('base/est/', views.stadistics, name='stadistics'),
    path('player/<slug:titulo>', views.player, name='player'),
    path('player/', views.player, name='player'),
    path('upload/', views.upload, name='upload'),
    path('__debug__/', include('debug_toolbar.urls')),
    #path('base/', views.base, name='base'),
    #path('base2/', views.base2, name='base2'),
]
