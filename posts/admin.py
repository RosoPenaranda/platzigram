''' Post admin classes'''

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models

from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  '''Post Admin model'''
  list_display = ('pk','user','photo')
  list_display_links = ('pk','user')
  list_editable = ('photo',)
  list_filter = ('created', 'modified')


