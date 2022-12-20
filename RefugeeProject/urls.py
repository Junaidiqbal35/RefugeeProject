from django.contrib import admin
from django.urls import path, include

from accounts.views import register, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/signup/", register, name='signup'),
    path("accounts/login/", login_view, name='login'),
    path("", include("core.urls")),
]
