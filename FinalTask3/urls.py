"""
FinalTask3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.urls import re_path

import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', authentication.views.login_page, name='login'),
    re_path(r'^logout$', authentication.views.logout_user, name='logout'),
    re_path(r'^index$', authentication.views.index, name='index'),
    re_path('signup', authentication.views.signup_page, name='signup'),
]