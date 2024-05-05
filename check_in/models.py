# models.py
from django.db import models
from django.conf import settings

class CheckIn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    check_out_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200)
    check_in_selfie = models.ImageField(upload_to='checkin_selfies/', blank=True, null=True)
    check_out_selfie = models.ImageField(upload_to='checkout_selfies/', blank=True, null=True)
