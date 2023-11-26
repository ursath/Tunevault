from django.urls import path, include
from . import views
from django.contrib import admin
from .views import vaultPost
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('music/<str:query>', views.music_search, name='music_search'),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('podcasts/<str:query>', views.podcasts_search, name='podcasts_search'),
    path('login/', views.signin, name='login'),
    path('create_account/', views.signup, name='create_account'),
    path('logout/', views.logout, name='logout'),
    path('members/', views.members, name='members'),
    path('members/<str:user>', views.member, name='member'),
    path('settings/', views.settings_profile, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('vault/<str:vtype>/<str:id>', views.vault, name='vault'),
    path('vault/<str:vtype>/<str:id>/post/<str:post_id>', vaultPost.as_view(), name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)