from rest_framework.routers import SimpleRouter

from apps.content.views import ContentViewSet

CONTENT_API = SimpleRouter()

CONTENT_API.register('content/content', ContentViewSet, basename='content-content')
