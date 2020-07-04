from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class followuser(models.Model):
    profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile")
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE)


class user_info(models.Model):

    user = models.CharField(max_length=60)
    college = models.CharField(max_length=90)
    year = models.CharField(max_length=40)

    def __str__(self):
        return str(self.user)+' from '+self.year
