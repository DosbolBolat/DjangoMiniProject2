from celery import shared_task
from django.core.mail import send_mail
from students.models import Student

@shared_task
def daily_attendance_reminder():
    # Логика для отправки напоминаний о посещаемости
    students = Student.objects.all()
    for student in students:
        send_mail(
            'Attendance Reminder',
            'Please mark your attendance for today.',
            'from@example.com',
            [student.user.email],
        )
    return f"Sent attendance reminders to {students.count()} students."

@shared_task
def grade_update_notification(student_email, grade, course_name):
    # Уведомление об изменении оценки
    send_mail(
        'Grade Updated',
        f'Your grade for {course_name} has been updated to {grade}.',
        'from@example.com',
        [student_email],
    )
    return f"Grade update notification sent to {student_email}."
