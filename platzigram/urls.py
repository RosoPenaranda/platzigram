''' URLs module'''

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
