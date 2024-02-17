from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.content.models import Content
from apps.content.serializers import ContentSerializer

class ContentViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        # Get the default context
        context = super().get_serializer_context()
        # Add or modify context as needed
        context['user'] = self.request.user
        return context
