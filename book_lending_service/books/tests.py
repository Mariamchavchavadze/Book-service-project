# books/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class BookApiTests(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='testuser@example.com'
        )


        self.token = self.get_jwt_token(self.user)


        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_jwt_token(self, user):
        """Utility method to get JWT token"""
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_create_book(self):

        url = '/api/books/'
        data = {'title': 'Test Book', 'author': 'Test Author', 'genre': 'Fiction', 'status': 'Available'}

        response = self.client.post(url, data, format='json', **self.headers)  # Use headers with token
        self.assertEqual(response.status_code, 201)  # Expecting 201 Created

    def test_get_books(self):

        url = '/api/books/'

        response = self.client.get(url, **self.headers)  # Use headers with token
        self.assertEqual(response.status_code, 200)  # Expecting 200 OK
