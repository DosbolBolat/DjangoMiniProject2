# Generated by Django 5.1.3 on 2024-11-16 07:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
