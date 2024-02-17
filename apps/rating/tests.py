import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from apps.content.models import Content
from apps.rating.models import Rating

class ContentViewSetTests(APITestCase):
    def setUp(self):
        
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.content = Content.objects.create(title='test content')
        
    def test_rating_return_unauthorized_error(self):
        url = reverse('rating-rating-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_rating_return_ok(self):
        self.client.force_login(user=self.user)
        url = reverse('rating-rating-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_new_rating_with_bad_rate(self):
            self.client.force_login(user=self.user)
            url = reverse('rating-rating-list')
            data = {
                 'content': self.content.id,
                 'user': self.user.id,
                 'rate': 6
            }
            response = self.client.post(url, data, format='json')

            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_new_rating(self):
            self.client.force_login(user=self.user)
            url = reverse('rating-rating-list')
            data = {
                 'content': self.content.id,
                 'user': self.user.id,
                 'rate': 2
            }
            response = self.client.post(url, data, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(Rating.objects.count(), 1)

    def test_create_new_duplicated_rating(self):
            self.client.force_login(user=self.user)
            url = reverse('rating-rating-list')
            data = {
                 'content': self.content.id,
                 'user': self.user.id,
                 'rate': 2
            }
            response = self.client.post(url, data, format='json')
            response = self.client.post(url, data, format='json')
            response = self.client.post(url, data, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(Rating.objects.count(), 1)

    def test_create_new_rating_update_rate_on_content(self):
            self.client.force_login(user=self.user)
            url = reverse('rating-rating-list')
            self.assertEqual(self.content.rating_average, 0)
            self.assertEqual(self.content.rating_count, 0)
            data = {
                 'content': self.content.id,
                 'user': self.user.id,
                 'rate': 2
            }
            response = self.client.post(url, data, format='json')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(Rating.objects.count(), 1)

            content = Content.objects.first()

            self.assertEqual(content.rating_average, 2)
            self.assertEqual(content.rating_count, 1)
