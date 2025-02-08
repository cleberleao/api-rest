"""
URL configuration for setup project.

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
from django.urls import path, include
from myflix.views import userViewSet, streamViewSet, listaViewSet, listaUser, listaStream
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', userViewSet, basename='users')
router.register('streams', streamViewSet, basename='streams')
router.register('listas',listaViewSet,basename='listas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('users/<int:pk>/listas/',listaUser.as_view()),
    path('streams/<int:pk>/listas/',listaStream.as_view()),
]
