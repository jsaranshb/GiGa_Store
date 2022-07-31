from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="UserProfile")
    address = models.TextField(null=True, blank=True)
    mobile = models.CharField(max_length=10)

    def __str__(self) -> str:
        return str(self.user)
    