from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger('student_management')


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        attendance = serializer.save()
        logger.info(
            f"Attendance marked: {attendance.student.name} - {attendance.status} for {attendance.course.name} on {attendance.date}"
        )
