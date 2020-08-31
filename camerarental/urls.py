"""camerarental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('send',views.send),
    path('camerarequest',views.camerarequest),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('login',views.login),
    path('registation',views.regist),
    path('register.html',views.register),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_form'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
