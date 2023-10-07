from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('settings/', views.settings_profile, name='settings'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('search', views.search_artist, name = 'search_artist'),
    path('vault/<str:pk>', views.vault, name='vault'),
]