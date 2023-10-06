
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tunevault import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileView, 'profile')
router.register(r'posts', views.PostView, 'post')
router.register(r'comments', views.CommentView, 'comment')
router.register(r'vaults', views.VaultView, 'vault')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tunevault.urls')),
    path('settings/', views.settings_profile, name='settings'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('search', views.search_artist, name = 'search_artist'),
    path('vault/<str:pk>', views.vault, name='vault'),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),    
    path('api/', include('tunevault.urls')),
    ]