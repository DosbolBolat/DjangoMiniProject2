from rest_framework import viewsets, status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']

    def update(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Student updated successfully",
            "data": serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return Response({
            "message": f"Student {student.name} deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)