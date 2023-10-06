
from django.contrib import admin
from django.urls import path, include
from tunevault import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tunevault.urls')),
    ]

# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)