from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('admins/users',views.get_users),
    path('admins/admins', views.get_admins),

    path('profile', views.profile),
    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),

]