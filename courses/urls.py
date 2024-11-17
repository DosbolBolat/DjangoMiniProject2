from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CourseViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('instructor/<int:instructor_id>/courses/', views.instructor_courses_view, name='instructor_courses'),
]