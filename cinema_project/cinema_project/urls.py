from django.contrib import admin
from django.urls import path
from cinema_project.api import api
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

