from rest_framework import viewsets
from .models import Grade
from .serializers import GradeSerializer
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('student_management')
class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        grade = serializer.save()
        logger.info(f"Grade updated: {grade.student.name} - {grade.grade} in {grade.course.name}")
        return grade

    def destroy(self, request, *args, **kwargs):
        grade = self.get_object()
        logger.info(f"Grade deleted: {grade.student.name} - {grade.grade} in {grade.course.name}")
        response = super().destroy(request, *args, **kwargs)
        return response