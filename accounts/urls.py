from django.urls import path
from main.views import home  # main 앱에서 home 뷰 임포트
from .views import login_view, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home, name='home'),  # /home/ URL에 대한 home 뷰 설정
]

