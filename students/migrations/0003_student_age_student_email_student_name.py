# Generated by Django 5.1.3 on 2024-11-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='Unnamed', max_length=100),
        ),
    ]
