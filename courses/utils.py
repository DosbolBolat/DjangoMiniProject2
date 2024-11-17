from django.core.cache import cache
from .models import Course

def get_courses_by_instructor(instructor_id):
    cache_key = f'courses_by_instructor_{instructor_id}'
    cached_courses = cache.get(cache_key)

    if cached_courses is None:
        courses = Course.objects.filter(instructor_id=instructor_id)
        cache.set(cache_key, courses, timeout=600)  # Кэшируем на 10 минут
        return courses

    return cached_courses