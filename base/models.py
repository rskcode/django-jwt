from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    account_type_choices = (
        ('student', 'Student'),
        ('parent', 'Parent'),
        ('teacher', 'Teacher'),
    )
    account_type = models.CharField(max_length=20, default='student', choices=account_type_choices)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()