from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('login/', views.signin, name='login'),
    path('create_account/', views.signup, name='create_account'),
    path('members/', views.members, name='members'),
    path('settings/', views.settings_profile, name='settings'),
    path('vault/<str:id>', views.vault, name='vault'),
]