from django.urls import path, re_path
from . import views

from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('login/', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('members/', views.members, name='members'),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]