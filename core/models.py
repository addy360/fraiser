from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
   

class Profile(models.Model):
    profile_img = models.FileField(upload_to="profiles")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.user.username


class Donation(models.Model):
    amount = models.CharField(max_length=10,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12,null=True)
    donator = models.CharField(max_length=255, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.transaction_id
 