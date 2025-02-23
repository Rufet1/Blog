"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from post.views import *
from django.conf.urls.static import static
from django.conf import settings
from profil.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('coronavirus/',corona_view, name = 'corona'),
    path('account/', include('accounts.urls')),
    path('profil/', include('profil.urls')),
    path('email/', include('sendemail.urls')),
    path('contact/', contact, name='contact'),
    path('', home_view, name="home"),
    path('about', about_view,name='about')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)