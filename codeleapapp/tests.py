from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import  Post

# Create your tests here.
class PostAPITestCase(APITestCase):

    def setUp(self):
        self.post = Post.objects.create(
            username="testuser",
            title="Title",
            content="Content"
        )
        self.valid_payload = {
            "username": "newuser",
            "title": "new title",
            "content": "new content"
        }
    
    def test_list_posts(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        response = self.client.post('/careers/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
    
    def test_find_id(self):
        response = self.client.get(f'/careers/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.post.username)

    def test_valid_patch(self):
        response = self.client.patch(f'/careers/{self.post.id}/', {
            "title": "Updated title"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated title")

    def test_invalid_patch(self):
        response = self.client.patch(f'/careers/{self.post.id}/', {
            "username": "ABC"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)
    
    def test_not_allowed_put(self):
        response = self.client.put(f'/careers/{self.post.id}/', {
            "title": "put test"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_post(self):
        response = self.client.delete(f'/careers/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())
