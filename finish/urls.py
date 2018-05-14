"""finish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from apps import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home-url'),
    path('login/', auth_views.login, {'template_name': 'login_templates/login_template.html'}, name = 'login_url'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name = 'logout_url'),
    path('sign-up/', views.sign_up, name = 'sign_up_url'),
    path('create/', views.CreateEntry, name = 'create_entry_url'),
    path('edit/(?P<entry_id>\d+)/', views.EditEntry, name = 'entry_url'),
    path('read/(?P<read_id>\d+)/', views.read_entry, name = 'read_url'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
