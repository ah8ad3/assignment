from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


from apps.rating.models import Rating
from apps.rating.serializers import RatingSerializer

class RatingViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # Automatically set the user ID from request.user when creating a new rating
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance: Rating = serializer.instance

        # add rate
        instance.content.add_rate(instance.rate)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
