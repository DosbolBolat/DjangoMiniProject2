from rest_framework.views import APIView
from rest_framework.response import Response
from .models import APIMetric, PopularCourse

class AnalyticsView(APIView):
    def get(self, request):
        api_metrics = APIMetric.objects.values('endpoint', 'method').count()
        popular_courses = PopularCourse.objects.order_by('-views')[:5]
        return Response({
            'api_metrics': api_metrics,
            'popular_courses': popular_courses.values('course__name', 'views'),
        })
