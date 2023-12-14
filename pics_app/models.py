from django.contrib.auth.models import User
from django.db import models
# from user_app.models import UserProfile

class Pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploaded_pics/')
    upload_time = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    # def __str__(self):
    #     return f"{self.user.username}'s Picture"
