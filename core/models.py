from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
   

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    profile_img = models.FileField(upload_to="profiles")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.user.username


class Donation(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.CharField(max_length=10,null=True)
    reference_number = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    mobile = models.CharField(max_length=12,null=True)
    donator = models.CharField(max_length=255, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.transaction_id
 