from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Post, Comment
from django.contrib.auth.models import User

class APITestCaseWithAuth(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user
        )

    def test_create_post(self):
        data = {
            'title': 'New Post',
            'content': 'This is a new post',
            'author': self.user.username,  # Передаем имя пользователя
        }
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_detail(self):
        response = self.client.get(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'author': self.user.username,  # Указываем имя автора
        }
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_post(self):
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
