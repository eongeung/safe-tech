from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # accounts 앱의 urls.py 포함
    path('', include('main.urls')),  # main 앱의 urls.py 포함
]
