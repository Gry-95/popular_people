from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path
from . import views
from .views import UserPasswordChange

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),  # users:login
    path('logout/', LogoutView.as_view(), name='logout'),  # users:logout
    path('password-change/', UserPasswordChange.as_view(), name='password_change'),  # users:logout
    path('password-change/done', PasswordChangeDoneView.as_view(
        template_name="users/password_change_done.html"), name='password_change_done'),  # users:logout
    path('register/', views.RegisterUser.as_view(), name='register'),  # users:register
    path('profile/', views.ProfileUser.as_view(), name='profile'),  # users:profile
]
