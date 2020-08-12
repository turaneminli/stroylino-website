from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    profile = models.ImageField(null=False, blank=True, upload_to='static/media')


