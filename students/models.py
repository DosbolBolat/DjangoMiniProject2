from django.db import models
from users.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, default='Unnamed')
    email = models.EmailField(unique=True, null=True, blank=True)  # Allow null values
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
