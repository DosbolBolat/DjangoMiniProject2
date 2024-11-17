from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from analytics import models
from analytics.models import PopularCourse
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from .utils import get_courses_by_instructor
from django.http import JsonResponse
import logging
from django.core.cache import cache

logger = logging.getLogger('student_management')

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        cached_courses = cache.get('courses')
        if cached_courses:
            logger.info("Cache hit: courses list")
            return Response(cached_courses)
        response = super().list(request, *args, **kwargs)
        cache.set('courses', response.data, timeout=3600)
        logger.info("Cache miss: courses list")
        return response

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        enrollment = serializer.save()
        logger.info(f"Student {enrollment.student.name} enrolled in course {enrollment.course.name}")

def instructor_courses_view(request, instructor_id):
    courses = get_courses_by_instructor(instructor_id)
    courses_data = list(courses.values())
    return JsonResponse(courses_data, safe=False)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        PopularCourse.objects.update_or_create(
            course=course,
            defaults={'views': models.F('views') + 1},
        )
        return super().retrieve(request, *args, **kwargs)