from pipes import Template
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.views.generic import TemplateView
from app_1.views import error_404handle, error_500handle

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('app_1.urls')),
]

handler404= error_404handle.as_view()
handler500= error_500handle.as_view()

