from django.contrib import admin
from django.urls import path, include

from finances.views import welcome_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome'),
    path('login/', login_view, name='login'),
    path('dashboard/', include('finances.urls')),
]
