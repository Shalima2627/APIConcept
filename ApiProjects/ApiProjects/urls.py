"""
URL configuration for ApiProjects project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from ApiApp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('admin/', admin.site.urls),
    path('', views.APITest.as_view(), name="test"),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('list-create/', views.PostListCreateView.as_view(), name='list-create'),
    path('api/token/', obtain_auth_token, name='obtain-token'),
]
