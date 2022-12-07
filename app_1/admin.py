from django.contrib import admin
from .models import Video, Channel, Comment


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
    ordering = ('channel_name',)
    search_fields = ('channel_name',)

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


#@admin.register(UploadVideo)  
#class UserAdmin(admin.ModelAdmin):
#    list_display = ('id', 'title', 'cathegory')
#    list_editable = ('title', 'cathegory',)
#    list_filter = ('cathegory',)
#    ordering = ('id', 'title')
#    search_fields = ('id', 'title')