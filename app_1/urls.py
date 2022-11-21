from django.urls import include, path
from . import views
from app_1.views import VideoListView, ProfileListView

#from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    #path('base/videos', views.base_main, name='videos'), 
    path('base/videos', VideoListView.as_view(), name='videos'),
    path('base2/profile/', ProfileListView.as_view(), name='profile'),
    path('player/<slug:titulo>', views.player, name='player'),
    path('player/', views.player, name='player'),
    path('upload/', views.upload, name='upload'),
    path('__debug__/', include('debug_toolbar.urls')),
    #path('base/', views.base, name='base'),
    #path('base2/', views.base2, name='base2'),
]
