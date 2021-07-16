from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_img = models.FileField(upload_to="profiles")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username