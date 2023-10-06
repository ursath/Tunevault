
from django.contrib import admin
from django.urls import path, include
from tunevault import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('settings/', views.settings_profile, name='settings'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('search', views.search_artist, name = 'search_artist'),
    path('vault/<str:pk>', views.vault, name='vault'),
]
