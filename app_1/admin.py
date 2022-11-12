from django.contrib import admin
from .models import User, Video, Channel, Comment


#MODIFICADO 

""" 
La administracion de los modelos se convierten en clases
Administracion del panel admin
Cambios en el listado de Videos
 """

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contrasenya')
    ordering = ('id', 'name')
    search_fields = ('id', 'name')

@admin.register(Video)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'path', 'thumnail', 'cathegory', 'length')
    list_editable = ('title', 'cathegory',)
    list_filter = ('cathegory',)
    ordering = ('id', 'title')
    search_fields = ('id', 'title')

@admin.register(Channel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel_name', 'subscribers')

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')



""" admin.site.register(User)
admin.site.register(Video) 
admin.site.register(Channel)"""
