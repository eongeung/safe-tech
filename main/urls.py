from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # 'login'으로 리다이렉트
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', login_required(views.home), name='home'),  # 로그인 필요
    path('support/', login_required(views.support_home), name='support_home'),  # 로그인 필요
    path('camera/', login_required(views.camera_integration), name='camera_integration'),  # 로그인 필요
    path('notifications/', login_required(views.notifications), name='notifications'),  # 로그인 필요
]
