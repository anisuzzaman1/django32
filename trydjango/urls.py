"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from accounts.views import (
    login_view,
    logout_view,
    register_view)
from .views import home_view # Import Views
from news import views

urlpatterns = [
    path('', home_view),   # Defined Index Page
    path('news/', views.news_search_view), # for Search View
    path('news/create/', views.news_create_view), # New Create Module
    path('news/<int:id>/', views.news_detail_view), # for new version
    path('admin/', admin.site.urls),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),
]