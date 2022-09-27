"""WordBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from WordsDRF.views import *
from SentencesDRF.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'word', WordAPIList, basename='Wolds_all')
router.register(r'Street',  WordAPIcategoryStreet, basename='Wolds_Street')
router.register(r'Home', WordAPIcategoryHome, basename='Wolds_Home')
router.register(r'Food', WordAPIcategoryFood, basename='Wolds_Food')
router.register(r'Sent', AccountViewSet, basename='Sent')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

