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
        content = Content.objects.create(title='test content')
        self.given_rate = 2
        Rating.objects.create(content=content, user=self.user, rate=self.given_rate)

    def test_content_return_unauthorized_error(self):
        url = reverse('content-content-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_content_return_ok(self):
        self.client.force_login(user=self.user)
        url = reverse('content-content-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_content_return_ok_with_user_rate(self):
            self.client.force_login(user=self.user)
            url = reverse('content-content-list')
            response = self.client.get(url, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            response_body = response.json()
            user_given_rate = response_body.get('results')[0].get('user_given_rate')
            self.assertEqual(user_given_rate, self.given_rate)
