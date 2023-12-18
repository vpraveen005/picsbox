from django.contrib.auth.models import User
from django.db import models


class Picture(models.Model):
    image = models.ImageField(upload_to='uploaded_pics/', max_length=500)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    upload_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)
