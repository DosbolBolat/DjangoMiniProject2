from .models import APIMetric

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/api/'):
            user = request.user if request.user.is_authenticated else None
            APIMetric.objects.create(
                user=user,
                endpoint=request.path,
                method=request.method,
            )
        return response
