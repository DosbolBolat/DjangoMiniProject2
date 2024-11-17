from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from students.models import Student

class StudentUpdateTest(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='password', role='teacher')
        self.student_user = User.objects.create_user(username='student', password='password', role='student')
        self.student = Student.objects.create(
            user=self.student_user,
            name='John Doe',
            email='john.doe@example.com',
            dob='2000-01-01'
        )
        self.client = APIClient()
        response = self.client.post('/auth/jwt/create/', {
            'username': 'teacher',
            'password': 'password'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_update_student_put(self):
        url = f'/api/students/{self.student.id}/'
        data = {
            "name": "Updated John Doe",
            "email": "updated.john@example.com",
            "dob": "2000-01-02"
        }
        response = self.client.put(url, data)
        print(response.data)
        updated_data = response.data.get('data')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(updated_data)
        self.assertEqual(updated_data.get('name'), "Updated John Doe")
        self.assertEqual(updated_data.get('email'), "updated.john@example.com")

    def test_update_student_patch(self):
        url = f'/api/students/{self.student.id}/'
        data = {
            "name": "Partially Updated Name"
        }
        response = self.client.patch(url, data)
        print(response.data)

        updated_data = response.data.get('data')
        self.assertIsNotNone(updated_data)
        self.assertEqual(updated_data.get('name'), "Partially Updated Name")


class StudentDeleteTest(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='password', role='teacher')
        self.student_user = User.objects.create_user(username='student', password='password', role='student')
        self.student = Student.objects.create(
            user=self.student_user,
            name='John Doe',
            email='john.doe@example.com',
            dob='2000-01-01'
        )
        self.client = APIClient()
        response = self.client.post('/auth/jwt/create/', {
            'username': 'teacher',
            'password': 'password'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_delete_student(self):
        url = f'/api/students/{self.student.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())
