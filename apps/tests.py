from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class HealthCheckViewTests(APITestCase):
    def test_health_check_returns_ok(self):
        url = reverse('health-check')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'status': 'ok'})

    def test_health_check_rejects_post(self):
        url = reverse('health-check')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class SchemaEndpointTests(TestCase):
    def test_schema_endpoint_returns_200(self):
        response = self.client.get('/api/schema/')

        self.assertEqual(response.status_code, 200)

    def test_swagger_ui_returns_200(self):
        response = self.client.get('/api/docs/')

        self.assertEqual(response.status_code, 200)


class TaskApiTests(APITestCase):
    def test_create_and_list(self):
        response = self.client.post('/api/tasks/', {'title': 'Birinchi'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data['is_done'])

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_blank_title_rejected(self):
        response = self.client.post('/api/tasks/', {'title': '   '}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_update_and_delete(self):
        task_id = self.client.post('/api/tasks/', {'title': 'A'}, format='json').data['id']

        response = self.client.patch(f'/api/tasks/{task_id}/', {'is_done': True}, format='json')
        self.assertTrue(response.data['is_done'])

        response = self.client.delete(f'/api/tasks/{task_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.client.get(f'/api/tasks/{task_id}/').status_code, 404)

    def test_filter_by_is_done(self):
        self.client.post('/api/tasks/', {'title': 'A', 'is_done': True}, format='json')
        self.client.post('/api/tasks/', {'title': 'B'}, format='json')

        response = self.client.get('/api/tasks/?is_done=true')
        self.assertEqual([t['title'] for t in response.data], ['A'])
