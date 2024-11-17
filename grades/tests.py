from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from students.models import Student
from courses.models import Course
from grades.models import Grade
from unittest.mock import patch

class GradeViewSetTest(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='password', role='teacher')
        self.student_user = User.objects.create_user(username='student', password='password', role='student')
        self.student = Student.objects.create(user=self.student_user, name='John Doe', email='john.doe@example.com', dob='2000-01-01')
        self.course = Course.objects.create(name='Math', description='Mathematics course', instructor=self.teacher)
        self.grade = Grade.objects.create(
            student=self.student,
            course=self.course,
            grade='B',
            teacher=self.teacher,
            date="2024-11-16"
        )
        response = self.client.post('/auth/jwt/create/', {
            'username': 'teacher',
            'password': 'password'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    @patch('grades.views.logger.info')
    def test_update_grade(self, mock_logger):
        url = f'/api/grades/{self.grade.id}/'
        data = {
            "student": self.student.id,
            "course": self.course.id,
            "grade": "A",
            "date": "2024-11-17",
            "teacher": self.teacher.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.grade.refresh_from_db()
        self.assertEqual(self.grade.grade, "A")
        self.assertEqual(self.grade.date.strftime("%Y-%m-%d"), "2024-11-17")
        mock_logger.assert_called_with(
            f"Grade updated: {self.grade.student.name} - {self.grade.grade} in {self.grade.course.name}"
        )

    @patch('grades.views.logger.info')
    def test_delete_grade(self, mock_logger):
        url = f'/api/grades/{self.grade.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Grade.objects.filter(id=self.grade.id).exists())

        mock_logger.assert_called_with(
            f"Grade deleted: {self.grade.student.name} - {self.grade.grade} in {self.grade.course.name}"
        )
