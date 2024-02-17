"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.content.urls import CONTENT_API
from apps.rating.urls import RATING_API

API = SimpleRouter()
API.registry.extend(CONTENT_API.registry)
API.registry.extend(RATING_API.registry)

api_urlpatterns = [
    path('v1/user/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('v1/user/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('v1/', include(API.urls), name="v1"),
]

urlpatterns = api_urlpatterns + [
    path('admin/', admin.site.urls),
]
