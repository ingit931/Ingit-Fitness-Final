from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout_user),
    
]