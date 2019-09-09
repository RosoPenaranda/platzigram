"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.urls import path
from django.contrib import admin

from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', local_views.helloWorld),
    path('hora/', local_views.time),
    path('hi/',local_views.hi),
    path('posts/', posts_views.list_posts),
    path("conf/qrconf.php", local_views.helloWorld)
]
