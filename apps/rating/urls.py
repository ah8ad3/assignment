from rest_framework.routers import SimpleRouter

from apps.rating.views import RatingViewSet

RATING_API = SimpleRouter()

RATING_API.register('rating/rating', RatingViewSet, basename='rating-rating')
